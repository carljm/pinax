"""
Utility classes and methods for Pinax' split-settings handling.

"""
import posixpath
import sys
from glob import glob
import os.path

class FakeModule(object):
    """
    A fake module where we only care about its __file__ attribute.

    Instantiated with a path and returns that path in response to any
    requested attribute (most importantly including __file__).

    """
    def __init__(self, path):
        self.path = path
        
    def __getattr__(self, key):
        return self.path


def get_settings(PROJECT_ROOT):
    """
    Given a directory path, execute all the .py files in that
    directory within the same local namespace, and then return that
    local namespace as a dictionary.

    """
    conffiles = glob(os.path.join(PROJECT_ROOT, 'conf', '*.py'))
    conffiles.sort()

    for f in conffiles:
        f = os.path.abspath(f)
        # probably better not to hack sys.modules unnecessarily
        if ('runserver' in sys.argv) or ('runserver_plus' in sys.argv):
            # sys.modules key doesn't matter as long as we avoid collisions
            sys.modules[f.replace(os.path.sep, '_')] = FakeModule(f)
        exec(open(f).read())

    return locals()
