#测试函数(name_function.py)
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + last
    return  full_name.title()

from chapter11 import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')

#可通过的测试
import unittest
from chapter11 import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_funciton.py"""

    def test_first_name(self):
        """能够正确地处理像Janis Joplin这样的名字吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEuqal(formatted_name, 'Janis Joplin')

unittest.main()

#不能通过的测试（修改）
#def get_formatted_name(first, middle, last):
#   """生成整洁的姓名"""
#    full_name = first + ' ' + middle + ' ' + last
#    return full_name.title()

import  unittest
from chapter11 import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart正阳的姓名吗？"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()

#方法名必须以test_打头，这样它才会在我们运行test_name_function.py时自动运行

#assertEqual(a, b)              核实a == b
#assertNotEqual(a, b)           核实a != b
#assertTrue(x)                  核实x为True
#assertFalse(x)                 核实x为False
#assertIn(item, list)           核实item在list中
#assertNotIn(item, list)        核实item不在list中

#一个要测试流的类
class AnonymousSurvey():

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results:")
        for response in responses:
            print('- ' + response)

from chapter11 import AnonymousSurvey

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\nThank you to everyon who participated in the survey!")
my_survey.show_results()

#测试AnonymousSurvey类
import unittest
from chapter11 import AnonymousSurvey

class TestAnonmyousSurcey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        question = "What language didi you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main()

import unittest
from survey import  AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def setUp(self):
        """
        创建一个调查对象和一组答案， 供使用的测试方法使用
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()