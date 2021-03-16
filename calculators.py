import re
def calculator(input_number):
    if input_number == "":
        return 0
    elif ',' in input_number and '\n' in input_number:
        nums = list(re.split(',|\n',input_number))
        result = float(nums[0]) + float(nums[1]) + float(nums[2])
    elif ',' in input_number:
        nums = input_number.split(',')
        result = float(nums[0]) + float(nums[1])
    elif '\n' in input_number:
        nums = input_number.split('\n')
        result = float(nums[0]) + float(nums[1])
    elif float(input_number) < 0:
        raise ValueError("Negative number occured")
    elif float(input_number) > 1000:
        return 0
    else:
        return float(input_number)
    return result

print(re.split(',|\n','30,50\n1'))