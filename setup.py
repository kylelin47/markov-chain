from setuptools import setup

setup(
    name='simplemarkov',
    version='0.1',
    install_requires=[
        'pymarkovchain ==1.7.5',
        'docopt ==0.6.2',
    ],
    scripts=[
        'markov/markov.py',
    ],
)
