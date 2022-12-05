import typing


def ask_attributes(quest_tpye: str, attribute: str, default_value: str) -> str:
    if quest_type == 'what':
        question = 'What ' + attribute + ' [' + default_value + ']? '
        choice = input(question)
    else:
        question = 'Has' + attribute + ' [' + default_value + ']? '
        choice = input(question)
    if choice == '':
        choice = default_value
    return choice


questions = ['color hair', 'hair length', 'color eyes', 'gender',
            'glasses', 'beard']

default_values = ['brown', 'short', 'blue', 'female',
            'no', 'no']

lenth = len(questions)
quest_type = ''
for i in range(lenth):
    if i < 4:
        quest_tpye = 'what'
    else:
        quest_type = 'has'
    choice = ask_attributes(quest_type, questions[i], default_values[i])
    print('You chose', choice)