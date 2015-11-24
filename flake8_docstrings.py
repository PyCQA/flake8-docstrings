# -*- coding: utf-8 -*-
"""pep257 docstrings convention needs error code and class parser for be
included as module into flake8
"""
import pep257

__version__ = '0.2.1.post1'


class pep257Checker(object):

    """flake8 needs a class to check python file."""

    name = 'pep257'
    version = __version__

    def __init__(self, tree, filename='(none)', builtins=None):
        self.tree = tree
        self.filename = filename

    def run(self):
        """Use directly check() api from pep257."""
        for error in pep257.check([self.filename]):
            # Ignore AllError, Environment error.
            if isinstance(error, pep257.Error):
                yield (error.line, 0, error.message, type(self))
