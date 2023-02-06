from typing import List
import sys

# my_file = open('lib.txt', 'r')
# # my_text = my_file.read()
# # print(my_text)

# # while True:
# #     line = my_file.readline()
# #     if line != '':
# #         print(line)
# #     else:
# #         break

# # for line in my_file:
# #     print(line)

# # for line in my_file.readlines():
# #     print(line)

# my_file.close()

def make_crazy_lib(filename: str) -> str:
    placeholders = ['NOUN', 'ADJECTIVE', 'VERB_ING', 'VERB']
    try:
        file = open(filename, 'r')

        text = ''

        for line in file:
            text = text + process_line(placeholders, line)
        
        file.close()

        return text
    except FileNotFoundError:
        print("Sorry, couldn't find", filename + '.')
    except IsADirectoryError:
        print('Sorry,',filename,'is a diretory.')
    except:
        print('Sorry, could not read', filename)

def process_line(placeholders: List[str],line: str) -> str:
    processed_line = ''

    words = line.split()

    for word in words:
        striped = word.strip('.,;?!')
        if striped in placeholders:
            answer = input(f'Enter a {striped}: ')
            processed_line = processed_line + answer

            if word[-1] in '.,;?!':
                processed_line = processed_line + word[-1] + ' '
            else:
                processed_line = processed_line + ' '

        else:
            processed_line = processed_line + word + ' '

    return processed_line + '\n'

def save_crazy_lib(filename: str, text: str) -> None:
    try:
        file = open(filename, 'w')
        file.write(text)
        file.close()
    except:
        print("Sorry, couldn't write file", filename)

def main() -> None:
    if len(sys.argv) != 2:
        print('crazy.py <filename>')
    else:
        filename = sys.argv[1]
        lib = make_crazy_lib(filename)
        # print(lib)
        if lib != None:
            save_crazy_lib('crazy_' + filename, lib)


if __name__ == "__main__":
    main()