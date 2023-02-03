



def is_plindrome(text: str) -> bool:
    if len(text) <= 1:
        return True
    elif text[0] == text[-1]:
        return is_plindrome(text[1:-1])
    else:
        return False

if __name__ == "__main__":
    text = 'tacocat'
    print(is_plindrome(text))
