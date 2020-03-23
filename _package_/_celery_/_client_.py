from datetime import datetime, timedelta

from _package_._celery_._task_ import add


def test_add():
    result = add.delay(2, 3)
    print("task id", result)
    print(result.get())
    print('over')


def test():
    """
    http://docs.celeryproject.org/en/latest/reference/celery.app.task.html#celery.app.task.Task.apply_async
    """

    # 5秒后执行任务
    add.apply_async(args=(2, 3), countdown=5)

    # 10秒后执行任务
    add.apply_async(args=[3, 7], eta=datetime.utcnow() + timedelta(seconds=10))

    # 10秒后过期
    add.apply_async(args=[3, 7], expires=10)


if __name__ == '__main__':
    print('start')
    test_add()
    print('end')
