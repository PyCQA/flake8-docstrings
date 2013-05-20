# -*- coding: utf-8 -*-
"""`flake8-docstring` lives on
`Bitbucket <https://bitbucket.org/icordasc/flake8-docstrings>`_.
"""

from setuptools import setup


def get_version(fname="flake8_docstrings/__init__.py"):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


def get_long_description():
    descr = []
    for fname in ('README.rst',):
        with open(fname) as f:
            descr.append(f.read())
    return '\n\n'.join(descr)

setup(name='flake8-docstrings',
      version=get_version(),
      description="Use pep257 static code analysis with flake8",
      long_description=get_long_description(),
      license='MIT',
      author='Simon ANDRÉ <sandre@anybox.fr>',
      url='https://bitbucket.org/icordasc/flake8-docstrings',
      classifiers=['Intended Audience :: Developers',
                   'Environment :: Console',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3',
                   'Operating System :: OS Independent',
                   'License :: OSI Approved :: MIT License'],
      keywords='PEP 257, pep257, PEP 8, pep8, docstrings, flake8',
      entry_points={'flake8.extension': [
                    'D = flake8_docstrings:_pep257.pep257Checker',
                    ],
                    },
      py_modules=['pep257'],
      install_requires=['flake8', 'pep257'],
      tests_require=['mock==0.8'])
