  # Program Name: Temp Coverter
# Program Purpose: Convert F to C or C to F
# Program Author: Victor Fries
# Date Completed: 11/5/24

# Declaring the function
def temp_converter(tempValue, unit):
    if unit == 'F':
        result = (tempValue * 9 / 5) + 32
    else: 
        result = (tempValue - 32) * 5 / 9
    return result

print(temp_converter(0, 'F'))
print(temp_converter(0,'C'))