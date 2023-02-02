def recursive_compute_sum(numlist):
    if len(numlist) == 0:
        return 0
    else:
        first = numlist[0]
        rest = numlist[1:]
        sum = first + recursive_compute_sum(rest)
        return sum


if __name__ == "__main__":
    numlist = [1, 2, 3, 4, 5, 6, 7,]
    print(recursive_compute_sum(numlist))