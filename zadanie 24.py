#24 Time for some fake graphics! Let’s say we want to draw game boards that look like this:
# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
"""--- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- --- """

size = int(input("Enter the size of the board"))


def print_rows():
    print((size) * " --- " )


def print_columns():
    print((size + 1) * "|    " )


for i in range(size):
    print_rows()
    print_columns()
print_rows()
