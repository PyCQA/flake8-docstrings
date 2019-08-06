# -*- coding: utf-8 -*-
"""``flake8-docstring`` lives on
`GitLab <https://gitlab.com/pycqa/flake8-docstrings>`_.
"""

from setuptools import setup


def get_version(fname="flake8_docstrings.py"):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


def get_long_description():
    descr = []
    for fname in ('README.rst', 'HISTORY.rst'):
        with open(fname) as f:
            descr.append(f.read())
    return '\n\n'.join(descr)


setup(
    name='flake8-docstrings',
    version=get_version(),
    description="Extension for flake8 which uses pydocstyle to check docstrings",
    long_description=get_long_description(),
    license='MIT License',
    author='Simon ANDRÉ',
    author_email='sandre@anybox.fr',
    maintainer='Ian Cordasco',
    maintainer_email='graffatcolmingov@gmail.com',
    url='https://gitlab.com/pycqa/flake8-docstrings',
    classifiers=['Intended Audience :: Developers',
                 'Environment :: Console',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 3',
                 'Operating System :: OS Independent',
                 'License :: OSI Approved :: MIT License'],
    keywords='PEP 257, pydocstyle, pep257, docstrings, flake8',
    entry_points={
        'flake8.extension': [
            'D = flake8_docstrings:pep257Checker',
        ],
    },
    install_requires=['flake8 >= 3', 'pydocstyle >= 2.1'],
    provides=['flake8_docstrings'],
    py_modules=['flake8_docstrings'],
)
