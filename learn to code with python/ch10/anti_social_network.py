users = {}

attributes = {
    'email': 'kim@oreilly.com',
    'gender': 'f',
    'age': 27,
    'friends': ['John', 'Josh']
}
users['Kim'] = attributes

users['John'] = {'email': 'john@abc.com', 'gender': 'm', 'age': 24, 'friends': ['Kim', 'Josh']}
users['Josh'] = {'email': 'josh@wickedlysmart.com', 'gender': 'm', 'age': 32, 'friends': ['Kim']}

# def average_age(name: str) -> None:
#     ages = [users[friend]['age'] for friend in users[name]['friends']]
#     friend_count = len(ages)
#     average_ages = sum(ages) / friend_count
#     print(f"{name}'s friends have an average age of {average_ages}")

# average_age('Kim')
# average_age('John')
# average_age('Josh')

max = 1000
for name in users:
    user = users[name]
    friends = user['friends']
    if len(friends) < max:
        most_anti_social = name
        max = len(friends)
print(f'The most_anti_social user is {most_anti_social}')