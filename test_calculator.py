import calculators as calc
import unittest
#An empty string returns zero

class TestStringMethods(unittest.TestCase): 
    def test_calculator(self):
    
        #Given
        input_number = ""
        expected_result = 0
        #When
        result = calc.calculator(input_number)
    
        #Then
        self.assertEqual(expected_result,result)
    def test2(self):
        input_number1 = '100'
        exp = 100

        result=calc.calculator(input_number1)

        self.assertEqual(exp,result)

    def test3(self):
        ssum = 100
        inp = '30,70'

        first_number = 60
        second_number = 40

        result = calc.calculator(inp)

        self.assertEqual(ssum,result)
    
    def test4(self):
        ssum = 100
        inp = '30\n70'

        result = calc.calculator(inp)

        self.assertEqual(ssum,result)
        
    def test5(self):
        ssum = 150
        inp = '30\n70,50'

        result = calc.calculator(inp)

        self.assertEqual(ssum,result)

        
if __name__ == '__main__': 
    unittest.main() 

