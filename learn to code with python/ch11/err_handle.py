# try:
#     filename = '\notthere'
#     file = open(filename, 'r')
# except FileNotFoundError:
#     print('Sorry,', filename, 'could not be found.')
# except (IsADirectoryError, OSError):
#     print("That's a directory not a file.")
# else:
#     print("It's a good thing we could open that file.")
#     file.close()
# finally:
#     print("I'm running no matter what happens.")

try:
    num = input('Got a number? ')
    result = 42 / int(num)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print('Excuse me, we asked for a number.')
else:
    print('Your answer is', result)
finally:
    print('Thanks for stopping by.')