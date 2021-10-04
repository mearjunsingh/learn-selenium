from programiz_python.programiz import PythonCompiler
import random


source_code1 = """

# Python Program to calculate the square root

# Note: change this value for a different result
num = 8 

# To take the input from the user
#num = float(input('Enter a number: '))

num_sqrt = num ** 0.5
print(num_sqrt)


"""

source_code2 = """

def add(a, b):
    return a + b


print(add(2, 3))

"""

source_code3 = """

# This program prints Hello, world!

print('Hello, world!')


"""


source_codes = [source_code1, source_code2, source_code3]


with PythonCompiler() as bot:
    bot.land_compiler()
    while True:
        source_code = random.choice(source_codes)
        bot.input_code(source_code)
        bot.render_code()
