'''
Запуск тестов doctest из unittest
'''

import doctest
import unittest
import doctest_4

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(doctest_4))     # файл с доктестами
    tests.addTests(doctest.DocFileSuite('prime.md'))    # файл с документацией
    return tests

if __name__ == '__main__':
    unittest.main()
