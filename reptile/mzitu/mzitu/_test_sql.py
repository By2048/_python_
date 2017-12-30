try:
    from .config import *
    from .all_class import *
except ImportError:
    from config import *
    from all_class import *

import sqlite3





has_down=get_has_down_by_sqlite()
print('\n'.join(has_down))


# all_meizi = []
# for item in has_down:
#     tmp = meizi_img(link=item[0].strip(), title=item[1].strip(), category=item[2].strip(), date=item[3].strip())
#     all_meizi.append(tmp)


# for item in all_meizi:
#     keep_has_down_to_sqlite(item)
#     item.print_all_info()
