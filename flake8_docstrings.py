# -*- coding: utf-8 -*-
"""pep257 docstrings convention needs error code and class parser for be
included as module into flakes8
"""
import pep257

__version__ = '0.1.2'


class pep257Checker(object):

    """flake8 needs a class to check python file."""

    name = 'pep257'
    version = __version__

    def __init__(self, tree, filename='(none)', builtins=None):
        self.tree = tree
        self.filename = filename

    def run(self):
        """Use directly check_source api from pep257."""
        self.messages = list()
        with open(self.filename, 'r') as fd:
            for elem in pep257.check_source(fd.read(), self.filename):
                self.messages.append(str(elem))

        for m in self.messages:
            log_mess = m.split(':')
            yield (int(log_mess[1]), int(log_mess[2]), log_mess[3][8:],
                   type(self))
