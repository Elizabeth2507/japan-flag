# patterns


def rectangle_border(N):
    string = ""
    # rectangle upper border
    for hash in range(0, 3 * N + 2):
        string += "#"
    string += "\n"

    return string


def rectangle_space(N):
    string = ""
    for row in range(0, int(N / 2)):
        string += "#"
        for space in range(0, 3 * N):
            string += " "
        string += "#"
        string += "\n"
    return string


def circle_upper_pattern(N):
    # **
    string = ""
    string += "#"
    for space_before in range(0, int(3 * N / 2 - 1)):  # 3 * n / 2   center by y axis
        string += " "
    string += "*" * 2
    for space_after in range(0, int(3 * N / 2 - 1)):
        string += " "
    string += "#"
    string += "\n"
    return string


def flag(N):
    str_output = ""
    rows = None

    if not isinstance(N, int):
        raise AssertionError("N should be integer.")

    if not N % 2 == 0:
        print("N should be odd value.")
        return
    elif N == 0:
        print("Zero is neither even, nor odd.")
        return

    str_output += rectangle_border(N)
    str_output += rectangle_space(N)
    # circle upper part
    str_output += circle_upper_pattern(N)

    # circle middle part

    for o_row in range(0, int((2 * N / 2 / 2) - 1)):
        str_output += "#"
        for space in range(0, int(3 * N / 2 - o_row - 2)):
            str_output += " "
        str_output += "*"
        for o in range(0, 2 * (o_row + 1)):
            str_output += "o"
        str_output += "*"
        for asterix in range(0, int(3 * N / 2 - o_row - 2)):
            str_output += " "
        str_output += "#"
        str_output += "\n"
        rows = o_row

    if isinstance(rows, int):

        for reflect_row in range(rows, -1, -1):
            str_output += "#"
            for ref_space in range(0, int(3 * N / 2 - reflect_row - 2)):
                str_output += " "
            str_output += "*"
            for ref_o in range(0, 2 * (reflect_row + 1)):
                str_output += "o"
            str_output += "*"
            for ref_asterix in range(0, int(3 * N / 2 - reflect_row - 2)):
                str_output += " "
            str_output += "#"
            str_output += "\n"

    # circle lower part
    str_output += circle_upper_pattern(N)

    str_output += rectangle_space(N)

    # rectangle upper border
    str_output += rectangle_border(N)

    return str_output


while True:
    print(flag(int(input("Enter N: "))))
