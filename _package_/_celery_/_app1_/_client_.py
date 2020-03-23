from _package_._celery_._app1_ import _task1_
from _package_._celery_._app1_ import _task2_

_task1_.add.apply_async(args=[2, 8])
_task1_.add.delay(2, 8)

_task2_.multiply.apply_async(args=[3, 7])

print('over')
