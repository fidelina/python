# Предположим, что есть функция c определенным поведением. Эту функцию
# очень любят давать на собеседованиях в качестве самой первой задачи.
# Я не опишу ее поведение, а лишь предоставлю тесты, которые она должна
# проходить. Вы должны на основе тестов написать исходную функцию.

def fizzbuzz(n):
    for i in range(n):
        if i % 15 == 0:
            print('FizzBizz')
        elif i % 3 == 0:

            print('Fizz')
        elif i % 5 == 0:
            print('Bizz')
        else:
            print(i)

import unittest

import main

class TestFizzBuzz(unittest.TestCase):

    def test_with_range(self):
        self.assertEqual(main.fizzbuzz(range(1, 21)),
                         [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8,
                          'Fizz', 'Buzz', 11, 'Fizz', 13, 14,
                          'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz'])

    def test_normal(self):
        self.assertEquals(main.fizzbuzz([1, 27, 45, 4, 7, 8, 9, 0]),
                          [1, 'Fizz', 'FizzBuzz', 4, 7, 8, 'Fizz', 'FizzBuzz'])

    def test_empty(self):
        self.assertListEqual(main.fizzbuzz([]), [])
