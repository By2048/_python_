import pickle
import logging


class Student(object):
    def __init__(self):
        self.name = '123'
        self.age = 123


def test_1():
    student = Student()
    logging.info(student)

    data = pickle.dumps(student)
    logging.info(f"{type(data)} {data}")


def test_2():
    data = b'\x80\x03c__main__\nStudent\nq\x00)\x81q\x01}q\x02(X\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00123q\x04X\x03\x00\x00\x00ageq\x05K{ub.'
    student = pickle.loads(data)
    logging.info(student)


if __name__ == '__main__':
    test_1()
    test_2()
