from setuptools import find_packages, setup

setup(
    name='markov-chain',
    version='0.1',
    install_requires=[
        'PyMarkovChain ==1.7.5',
        'Docopt ==0.6.1',
    ],
    packages=find_packages(),
    scripts=[
        'markov/markov.py',
    ],
)
