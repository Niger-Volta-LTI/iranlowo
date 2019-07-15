import os

module_path = os.path.dirname(__file__)  # needed because sample data files are located in the same folder


def datapath(fname=None):
    if not fname:
        return os.path.join(module_path, 'testdata')
    return os.path.join(module_path, 'testdata', fname)
