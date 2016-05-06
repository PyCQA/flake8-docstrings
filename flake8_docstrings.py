# -*- coding: utf-8 -*-
"""Implementation of pydocstyle integration with Flake8.

pydocstyle docstrings convention needs error code and class parser for be
included as module into flake8
"""
import sys

import pep8
try:
    import pycodestyle as pydocstyle
except ImportError:
    import pydocstyle

__version__ = '0.2.6'
__all__ = ['pydocstyleChecker']


class EnvironError(pydocstyle.Error):
    code = 'D998'
    context = None

    @property
    def short_desc(self):
        return sys.exc_info()[1]


class AllError(pydocstyle.Error):
    code = 'D999'
    short_desc = '__all__ was found to be a list or other mutable collection'
    context = None


class pydocstyleChecker(object):
    """Flake8 needs a class to check python file."""

    name = 'flake8-docstrings'
    version = __version__ + ', pydocstyle: {0}'.format(pydocstyle.__version__)

    STDIN_NAMES = set(['stdin', '-', '(none)', None])

    def __init__(self, tree, filename='(none)', builtins=None):
        """Placeholder."""
        self.tree = tree
        self.filename = filename
        self.checker = pydocstyle.PEP257Checker()
        self.load_source()

    def _check_source(self):
        try:
            return list(self.checker.check_source(self.source, self.filename))
        except pydocstyle.AllError as err:
            return [AllError(err)]
        except EnvironmentError as err:
            return [EnvironError(err)]

    def run(self):
        """Use directly check() api from pydocstyle."""
        checked_codes = pydocstyle.conventions.pep257
        for error in self._check_source():
            if isinstance(error, pydocstyle.Error) and error.code in checked_codes:
                # NOTE(sigmavirus24): Fixes GitLab#3
                message = '%s %s' % (error.code, error.short_desc)
                yield (error.line, 0, message, type(self))

    def load_source(self):
        """Load the source for the specified file."""
        if self.filename in self.STDIN_NAMES:
            self.filename = 'stdin'
            self.source = pep8.stdin_get_value()
        else:
            with pydocstyle.tokenize_open(self.filename) as fd:
                self.source = fd.read()
