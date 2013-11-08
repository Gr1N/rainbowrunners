# -*- coding: utf-8 -*-

import time
import unittest

__all__ = (
    'Tests',
)


class Tests(unittest.TestCase):
    pass


def test_generator():
    def test(self):
        time.sleep(0.15)
    return test


for i in range(20):
    test_name = 'test_%s' % i
    test = test_generator()
    setattr(Tests, test_name, test)
