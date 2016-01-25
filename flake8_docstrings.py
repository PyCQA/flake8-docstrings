# -*- coding: utf-8 -*-
"""Implementation of pep257 integration with Flake8.

pep257 docstrings convention needs error code and class parser for be
included as module into flake8
"""
import io

import pep8
import pep257

__version__ = '0.2.4'
__all__ = ['pep257Checker']


class pep257Checker(object):
    """Flake8 needs a class to check python file."""

    name = 'flake8-docstrings'
    version = __version__ + ', pep257: {0}'.format(pep257.__version__)

    STDIN_NAMES = set(['stdin', '-', '(none)', None])

    def __init__(self, tree, filename='(none)', builtins=None):
        """Placeholder."""
        self.tree = tree
        self.filename = filename
        self.checker = pep257.PEP257Checker()
        self.load_source()

    def run(self):
        """Use directly check() api from pep257."""
        try:
            return self._run()
        except (pep257.EnvironmentError, pep257.AllError) as err:
            message = 'D999 %s' % err
            return iter([(1, 0, message, type(self))])

    def _run(self):
        checked_codes = pep257.conventions.pep257
        for error in self.checker.check_source(self.source, self.filename):
            # Ignore AllError, Environment error.
            if isinstance(error, pep257.Error) and error.code in checked_codes:
                # NOTE(sigmavirus24): Fixes GitLab#3
                message = '%s %s' % (error.code, error.short_desc)
                yield (error.line, 0, message, type(self))

    def load_source(self):
        """Load the source for the specified file."""
        if self.filename in self.STDIN_NAMES:
            self.filename = 'stdin'
            self.source = pep8.stdin_get_value()
        else:
            with io.open(self.filename, encoding='utf-8') as fd:
                self.source = fd.read()
