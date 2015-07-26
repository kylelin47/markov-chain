"""Usage:
    markov.py <input_file>... [-o <output_file>] [-s <num>] [-d <db_name>]
    markov.py [-o <output_file>] [-s <num>] [-d <db_name>]
    markov.py -h | --help
Options:
    -h --help         show this help message
    -o <output_file>  file to place output text
    -s <num>          number of strings to generate [default: 50]
    -d <db_name>      database to use [default: ./markov_db]
"""
from docopt import docopt
from pymarkovchain import MarkovChain

def generate_markov_chain(args):
    mc = MarkovChain(args['-d'])
    text = read_from_files(args['<input_file>'])
    mc.generateDatabase(text)
    return mc

def output_markov_text(args, mc):
    num_lines = args['-s']
    if args['-o']:
        with open(args['-o'], 'w') as output_file:
            output_text_to_file(
                num_lines, mc.generateString,
                output_file=output_file)
    else:
        output_text_to_file(num_lines, mc.generateString)

def output_text_to_file(num_lines, text_generator, output_file=None):
    for i in range(0, num_lines):
        print(text_generator(), file=output_file)

def read_from_files(file_names):
    text = ""
    for file_name in file_names:
        with open(file_name) as file:
            text += file.read().replace('\n', ' ')
    return text

if __name__ == '__main__':
    args = docopt(__doc__)
    args['-s'] = int(args['-s'])

    if args['<input_file>']:
        mc = generate_markov_chain(args)
    else:
        mc = MarkovChain(args['-d'])
    output_markov_text(args, mc)
