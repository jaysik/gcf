# This is to calculate the Greatest Common Factor of two numbers.
# This loops through the division of the two numbers until no reminader remains.

# Call this file in the console command: "python GCF.py" and follow the prompts.

import math

# Title
print("""
      Greatest Common Factor Calculator

    Find the highest divisor of two numbers
""")

# User inputs
val1 = int(input("Please enter the first number: "))
val2 = int(input("Enter the second number: "))

print('') # To provide console spacing.

largerNumber = val1
smallerNumber = val2

# Place the numbers in the right functions
if (val1 < val2):
    largerNumber = val2
    smallerNumber = val1

def calculate():
    prevModulus = smallerNumber
    modulus = largerNumber % smallerNumber
    step = 1

    while (modulus > 0):
        newModulus = prevModulus % modulus
        if (step == 1):
            print(step, "-", largerNumber, "/", smallerNumber, "=", largerNumber/smallerNumber, '[ modulus =', modulus, "]")
        else:
            print(step, "-", prevModulus, "/", modulus, "=", prevModulus/modulus, '[ modulus =', newModulus, "]")

        prevModulus = modulus
        modulus = newModulus
        step += 1
        if newModulus == 0:
            gcfFound(prevModulus)
            break
    else:
        if (modulus == 0):
            gcfFound(prevModulus)
        else:
            print('No GFC found!', modulus)

def gcfFound(value):
    print("")
    print('The GCF is:', value)
    print('')
    print('Final Results:')
    print(val1, "==>", math.trunc(val1/value))
    print(val2, "==>", math.trunc(val2/value))
    print('')

calculate()