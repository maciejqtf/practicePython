winner_is_2 = \
    [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = \
    [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = \
    [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = \
    [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = \
    [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]


def check_winner(game):

    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2]  != 0:
            return game[i][0]
        elif game[0][i] == game[1][i] == game[1][i]  != 0:
            return game[0][i]
    if game[0][0] == game[1][1] == game[2][2] or game[0][2] == game[1][1] == game[2][0]:
        return game[1][1]
    else:
        return 0

print(check_winner(winner_is_2))
print(check_winner(winner_is_1))
print(check_winner(no_winner))


def max_number(a=1,b=2,c=3):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(max_number())
print(max_number(3,5,7))
print(max_number(9,3,5))
print(max_number(45,3546,456))