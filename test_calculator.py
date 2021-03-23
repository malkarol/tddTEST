import calculators as calc
import unittest
#An empty string returns zero

class TestStringMethods(unittest.TestCase): 
    def testEmptyString(self):
        input_string = ""
        expected_result = 0

        result = calc.calculate(input_string)

        self.assertEqual(expected_result,result)

    def testSingleNumber(self):
        input_string = '100'
        expected_result = 100

        result=calc.calculate(input_string)

        self.assertEqual(expected_result,result)

    def testCommaSepNumbers(self):
        input_string = '30,70'
        expected_result = 100

        result = calc.calculate(input_string)

        self.assertEqual(expected_result,result)
    
    def testNewLSepNumbers(self):
        input_string = '30\n70'
        expected_result = 100

        result = calc.calculate(input_string)

        self.assertEqual(expected_result, result)

    def testThreeNumsSep(self):
        input_string = '30\n70,50'
        expected_result = 150

        result = calc.calculate(input_string)

        self.assertEqual(expected_result, result)


    def testNegativeNum(self):
        input_string = '-100'
        expected_result = ValueError
        
        result = calc.calculate(input_string)

        self.assertEqual(expected_result, type(result))


    def testNumOverflow(self):
        input_string = '1200'
        expected_result = 0

        result = calc.calculate(input_string)

        self.assertEqual(result, expected_result)

    def testCustomSep(self):
        input_string = '//#\n120,30#50'
        expected_result = 200

        result = calc.calculate(input_string)

        self.assertEqual(result, expected_result)

    def testCustomSingleSep(self):
        input_string = '//[#]\n150\n20#30'
        expected_result = 200

        result = calc.calculate(input_string)

        self.assertEqual(result, expected_result)

    def testCustomMultiSep(self):
        input_string = '//[##][@]\n100,20\n30##10@40'
        expected_result = 200

        result = calc.calculate(input_string)

        self.assertEqual(result, expected_result)

    
        
if __name__ == '__main__': 
    unittest.main() 

