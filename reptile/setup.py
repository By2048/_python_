import logging
import datetime

from mzitu.main import main
from mzitu.config import download_path

if __name__ == '__main__':
    logging.info('start mzitu         {}'.format(datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')))
    logging.info('download_path       {}'.format(download_path))
    main()
