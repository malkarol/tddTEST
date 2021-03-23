import re

def validate_number(num):
    if float(num) > 1000:
        return 0
    elif float(num) < 0:
        return ValueError("Negative Number Occured")
    else: 
        return float(num)


def calculate(input_number):
    if input_number == "":
        return 0

    if not input_number.startswith('//'):
        nums = list(re.split(',|\n',input_number))

        if len(nums) == 1:
            return validate_number(nums[0])
        else:
            nums = [float(i) for i in nums]
            return sum(nums)

    nums = input_number.split('\n', 1)
    numbers_string = nums[1]
    delims = nums[0].split('//')
    delims = delims[1:len(delims)]
    numbers = list()
    if not delims[0].startswith('['):
        numbers = list(re.split(',|\n|'+ delims[0],numbers_string))
    else:
        delims = delims[0].split('[')
        delims = [x for x in delims if x]
        filterstring = r',|\n'
        for delim in delims:
            filterstring += '|' + delim[:-1]
        numbers = list(re.split(filterstring, numbers_string))

    numbers = [validate_number(float(i)) for i in numbers]        
    return sum(numbers)

    
        
