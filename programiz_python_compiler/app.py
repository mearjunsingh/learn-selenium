from programiz_python.programiz import PythonCompiler


source_code = """

def add(a, b):
    return a + b


print(add(3, 3))

"""


with PythonCompiler() as bot:
    bot.land_compiler()
    bot.input_code(source_code)
    bot.render_code()
