# Setup scores of all Bubbles-R-Us tests
scores = [60, 50, 60, 58, 54, 54,
            58, 50, 52, 54, 48, 69,
            34, 55, 51, 52, 44, 51,
            69, 64, 66, 55, 52, 61,
            46, 31, 57, 52, 44, 18,
            41, 53, 55, 61, 51, 44]

# # Listing all the solution and their corresponding scores
# # For loop version
# for i, score in enumerate(scores):
#     print('Bubble solution #'+str(i), 'score:', score)
# print('Bubbles tests:', len(scores))
# print('Highest bubble score:', max(scores))

# While loop version
i = 0
test_times = len(scores)
while i < test_times:
    print('Bubble solution #'+str(i), 'score:', scores[i])
    i += 1
print('Bubbles tests:', test_times)
print('Highest bubble score:', max(scores))
