# Add type annotations to the three functions shown below.

def multiply(num1: int, num2: int):
    return num1 * num2

def greet(greeting: str, name: str):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def shopping_list(*args:str):
    [print(f"* {item}") for item in args]
    return args

print(multiply(1,2))
print(greet("hi","you"))
print(shopping_list("toys","chocolate","pens"))
