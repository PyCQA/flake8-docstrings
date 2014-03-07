# -*- coding: utf-8 -*-
"""pep257 docstrings convention needs error code and class parser for be
included as module into flakes8
"""
import pep257

__version__ = '0.2.0'


class pep257Checker(object):

    """flake8 needs a class to check python file."""

    name = 'pep257'
    version = __version__

    def __init__(self, tree, filename='(none)', builtins=None):
        self.tree = tree
        self.filename = filename

    def run(self):
        """Use directly check_source api from pep257."""
        errors = list()
        with open(self.filename, 'r') as handle:
            for error in pep257.PEP257Checker().check_source(
                    handle.read(), self.filename):
                errors.append(error)

        for error in errors:
            yield (error.line, 0, error.message, type(self))
