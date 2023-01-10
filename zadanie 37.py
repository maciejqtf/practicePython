# 37 Refactor existing code snippet into function

"""print(" --- --- ---")
print("|   |   |   |")
print(" --- --- ---")
print("|   |   |   |")
print(" --- --- ---")
print("|   |   |   |")
print(" --- --- ---")"""


def print_vertical(size):
    sign = "|"
    for i in range(size):
        sign += "   |"
    print(sign)


def print_horizontal(size):
    sign = ""
    for i in range(size):
        sign += " ---"
    print(sign)

size = 5
print_horizontal(size)
for i in range(size):
    print_vertical(size)
    print_horizontal(size)