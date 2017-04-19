# -*- coding: utf-8 -*-
"""Implementation of pydocstyle integration with Flake8.

pydocstyle docstrings convention needs error code and class parser for be
included as module into flake8
"""
import sys

from flake8_polyfill import stdin
import pycodestyle
try:
    import pydocstyle as pep257
    module_name = 'pydocstyle'
except ImportError:
    import pep257
    module_name = 'pep257'

__version__ = '1.0.3'
__all__ = ('pep257Checker',)

stdin.monkey_patch('pycodestyle')


class EnvironError(pep257.Error):
    code = 'D998'
    context = None

    @property
    def short_desc(self):
        return sys.exc_info()[1]


class AllError(pep257.Error):
    code = 'D999'
    short_desc = '__all__ was found to be a list or other mutable collection'
    context = None


class pep257Checker(object):
    """Flake8 needs a class to check python file."""

    name = 'flake8-docstrings'
    version = __version__ + ', {0}: {1}'.format(
        module_name, pep257.__version__
    )

    STDIN_NAMES = set(['stdin', '-', '(none)', None])

    def __init__(self, tree, filename='(none)', builtins=None):
        """Placeholder."""
        self.tree = tree
        self.filename = filename
        self.checker = pep257.ConventionChecker()
        self.load_source()

    def _check_source(self):
        try:
            # TODO: Naive fix for `pydocstyle 2.0.0` with default settings.
            # Should probably add a proper setting so `ignore_decorators` can
            # be set when caling through the CLI
            return list(self.checker.check_source(
                self.source,
                self.filename,
                ignore_decorators=None,
            ))
        except pep257.AllError as err:
            return [AllError(err)]
        except EnvironmentError as err:
            return [EnvironError(err)]

    def run(self):
        """Use directly check() api from pydocstyle."""
        checked_codes = pep257.conventions.pep257
        for error in self._check_source():
            if isinstance(error, pep257.Error) and error.code in checked_codes:
                # NOTE(sigmavirus24): Fixes GitLab#3
                message = '%s %s' % (error.code, error.short_desc)
                yield (error.line, 0, message, type(self))

    def load_source(self):
        """Load the source for the specified file."""
        if self.filename in self.STDIN_NAMES:
            self.filename = 'stdin'
            self.source = pycodestyle.stdin_get_value()
        else:
            with pep257.tokenize_open(self.filename) as fd:
                self.source = fd.read()
