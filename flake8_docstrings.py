# -*- coding: utf-8 -*-
"""pep257 docstrings convention needs error code and class parser for be
included as module into flake8
"""
import io

import pep8
import pep257

__version__ = '0.2.2'


class pep257Checker(object):

    """flake8 needs a class to check python file."""

    name = 'pep257'
    version = __version__

    STDIN_NAMES = set(['stdin', '-', '(none)', None])

    def __init__(self, tree, filename='(none)', builtins=None):
        self.tree = tree
        self.filename = filename
        self.source = self.load_source()
        self.checker = pep257.PEP257Checker()

    def run(self):
        """Use directly check() api from pep257."""
        for error in self.checker.check_source(self.source, self.filename):
            # Ignore AllError, Environment error.
            if isinstance(error, pep257.Error):
                yield (error.line, 0, error.message, type(self))

    def load_source(self):
        if self.filename in self.STDIN_NAMES:
            self.filename = 'stdin'
            self.source = pep8.stdin_get_value()
        else:
            with io.open(self.filename, encoding='utf-8') as fd:
                self.source = fd.read()
