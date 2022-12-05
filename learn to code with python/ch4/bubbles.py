# Setup scores of all Bubbles-R-Us tests
scores = [60, 50, 60, 58, 54, 54,
            58, 50, 52, 54, 48, 69,
            34, 55, 51, 52, 44, 51,
            69, 64, 66, 55, 52, 61,
            46, 31, 57, 52, 44, 18,
            41, 53, 55, 61, 51, 44]

costs = [.25, .27, .25, .25, .25, .25,
            .33, .31, .25, .29, .27, .22,
            .31, .25, .25, .33, .21, .25,
            .25, .25, .28, .24, .25, .22,
            .20, .25, .30, .25, .24, .25,
            .25, .25, .27, .25, .26, .29]

# # While loop version
# i = 0
# test_times = len(scores)
# while i < test_times:
#     print('Bubble solution #'+str(i), 'score:', scores[i])
#     i += 1
# print('Bubbles tests:', test_times)
# print('Highest bubble score:', max(scores))

# Listing all the solution and their corresponding scores
# For loop version
best_solutions = []
highest_score = 0
for i, score in enumerate(scores):
    print('Bubble solution #'+str(i), 'score:', score)
    if score > highest_score:
        highest_score = score

print('Bubbles tests:', len(scores))
print('Highest bubble score:', max(scores))

for i in range(len(scores)):
    if scores[i] == highest_score:
        best_solutions.append(i)
print('Solutions with the highest score:', best_solutions)

cost = 100.0
most_effective = 0

for i in range(len(best_solutions)):
    index = best_solutions[i]
    if cost > costs[index]:
        most_effective = index
        cost = costs[index]

print('Solution', most_effective, 'is the most effective with a cost of', cost)