import random

WIDTH: int = 100

moves: list[str] = ["straight_short", "straight_long",
                    "bend_left_short", "bend_left_long",
                    "bend_right_short", "bend_right_long"]

# Make sure 'shrek.txt' is in the same directory.
f = open("shrek.txt", mode='r')


def will_hit_edge(move: str, pos: int) -> bool:
    match move:
        case "bend_left_short":
            pos -= 1
        case "bend_left_long":
            pos -= 2
        case "bend_right_short":
            pos += 1
        case "bend_right_long":
            pos += 2

    return pos <= 1 or pos >= (WIDTH - 1)


def draw_snake_segment(pos: int, move: str) -> int:
    left_whitespace: str = " " * (pos - 2)
    match move:
        case "straight_short":
            print(left_whitespace + "|``|" + f.readline().rstrip("\n"))

        case "straight_long":
            print(left_whitespace + "|``|" + f.readline().rstrip("\n"))
            print(left_whitespace + "|``|" + f.readline().rstrip("\n"))

        case "bend_left_short":
            print(left_whitespace + "/''/" + f.readline().rstrip("\n"))
            print(" " * (pos - 3) + "|``|" + f.readline().rstrip("\n"))
            pos -= 1

        case "bend_left_long":
            print(left_whitespace + "/''/" + f.readline().rstrip("\n"))
            print(" " * (pos - 3) + "/''/" + f.readline().rstrip("\n"))
            pos -= 2

        case "bend_right_short":
            print(left_whitespace + "\\``\\" + f.readline().rstrip("\n"))
            print(left_whitespace + " " + "|``|" + f.readline().rstrip("\n"))
            pos += 1

        case "bend_right_long":
            print(left_whitespace + "\\``\\" + f.readline().rstrip("\n"))
            print(left_whitespace + " " + "\\``\\" + f.readline().rstrip("\n"))
            pos += 2

    return pos


def main():
    pos: int = random.randint(2, WIDTH - 2)
    i: int = 0
    while True:
        i += 1
        if i % 10000000 == 0:
            move: str = random.choice(moves)
            while will_hit_edge(move, pos):
                move = random.choice(moves)

            pos = draw_snake_segment(pos, move)
            i = 0


if __name__ == "__main__":
    main()
