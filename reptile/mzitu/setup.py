try:
    from mzitu.mzitu import *
except ImportError:
    from .mzitu.mzitu import *

if __name__=='__main__':
    start_mzitu()