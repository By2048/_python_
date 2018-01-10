import sys

try:
    from .mzitu.main import *
except ImportError:
    from mzitu.main import *

if __name__ == '__main__':
    start_mzitu()
