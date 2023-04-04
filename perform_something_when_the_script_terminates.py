from atexit import register

@register
def terminate():
    print("Goodbye!")

while True:
    print("Hello")
