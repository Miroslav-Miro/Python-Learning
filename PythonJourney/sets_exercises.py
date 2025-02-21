friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

cars_set = set(cars)
print(cars_set)

# Check if ‘Eric’ and ‘John’ exist in friends
print('Eric' in friends)
print('John' in friends)

friends_unu = friends.union(my_friends)
print(friends_unu)

names = friends.intersection(my_friends)
print(names)

names_diff = friends.difference(my_friends)
print(names_diff)