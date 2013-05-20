# -*- coding: utf-8 -*-
"""pep257 docstrings convention needs error code and class parser for be
included as module into flakes8
"""
__version__ = "0.1"
from pep257 import check_source


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
        for elem in check_source(
                open(self.filename, 'r').read(), self.filename):
            self.messages.append(str(elem))
        for m in self.messages:
            log_mess = m.split(':')
            yield int(log_mess[1]), int(log_mess[2]), \
                log_mess[3].strip(), type(self)
