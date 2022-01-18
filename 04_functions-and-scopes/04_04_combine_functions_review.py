# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

import write_letter_done
def greet(greeting, name):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def write_letter(name, text):
    print(f"Hi {name}.")
    print(f"Bye {name}. {text}")

write_letter(greet(greeting="hello", name="Jonathan"), "Welcome")