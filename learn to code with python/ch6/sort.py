from typing import *


# Bubble sort function
def bubble_sort(scores: List, index_list: List, inverse: bool = False) -> None:
    swapped = True

    if inverse:
        while swapped:
            swapped = False

            for i in range(len(scores)-1):
                if scores[i] < scores[i+1]:
                    temp = scores[i]
                    scores[i] = scores[i+1]
                    scores[i+1] = temp
                    temp = index_list[i]
                    index_list[i] = index_list[i+1]
                    index_list[i+1] = temp
                    swapped = True
    else:
        while swapped:
            swapped = False

            for i in range(len(scores)-1):
                if scores[i] > scores[i+1]:
                    temp = scores[i]
                    scores[i] = scores[i+1]
                    scores[i+1] = temp
                    temp = index_list[i]
                    index_list[i] = index_list[i+1]
                    index_list[i+1] = temp
                    swapped = True


# Setup scores of all Bubbles-R-Us tests
scores = [60, 50, 60, 58, 54, 54,
            58, 50, 52, 54, 48, 69,
            34, 55, 51, 52, 44, 51,
            69, 64, 66, 55, 52, 61,
            46, 31, 57, 52, 44, 18,
            41, 53, 55, 61, 51, 44]

number_of_scores = len(scores)
solution_numbers = list(range(number_of_scores))

bubble_sort(scores, solution_numbers)
# print(scores)
bubble_sort(scores, solution_numbers, inverse=True)
# print(scores)

print('Top Bubble Solutions')
for i in range(5):
    print(str(i+1)+')', 'Bubble Solution', '#'+str(solution_numbers[i]), 'score:', scores[i])