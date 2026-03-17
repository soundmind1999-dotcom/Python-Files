from unittest import TestCase
class TestDivisionsFunctions(TestCase)
    def test_that_the_first_number_can_be_divided_by_second_number(self):
    result = divisions_functions.check_if_first_number_can_be_divided_by_second_number(20, 5)
    self.assertEqual(result,True)
    self.assertEqual(test_functions_divisions.check_if_first_number_can_be_divided_by_second_number(10, 2), True)


    def test_that_the_second_number_is_between_2_and_36(self):
    result = divisions_functions.the_second_number_is_between_2_and_36(300, 1) #too small
    result_two = divisions_functions.the_second_number_is_between_2_and_36 (300, 40) #too large
    self.assertEqual(result,True)
    self.assertEqual(result_two,True)
    self.assertEqual(test_functions_divisions.check_if_first_number_can_be_divided_by_second_number(10, 2), True)

