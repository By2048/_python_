import logging
import logging.config

logging.basicConfig(level=logging.INFO)

from colorama import Fore, Back, Style

logging.info(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
