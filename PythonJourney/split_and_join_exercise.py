csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
print(csv)
friends_list = ['Exercise: fill me with names']


friends_list = csv.split(':')
print(friends_list)

friends_list_2 = friends_list[1].split(';')
friends_list.pop(1)
print(friends_list)
print(friends_list_2) 

friends_list = (f'{friends_list[0]},{friends_list_2[0]},{friends_list_2[1]}')
friends_list = friends_list.split(',')
print(friends_list)

my_test = csv.replace(':',',').replace(';',',').split(',')
print(my_test)