def read_lines(path):
    with open(path) as f:
        data = f.readlines()
        lines = len(data)
        return lines


def divide(length):
    if length % 2 == 0:
        firstpart, secondpart = length // 2, length // 2
        return firstpart, secondpart
    else:
        firstpart, secondpart = length // 2, length // 2 + 1
        return firstpart, secondpart
