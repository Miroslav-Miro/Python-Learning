names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

all_names = names + names1

# INPUT 2 names more
for _ in range(2):
  input_name = input('Enter a name: ')
  all_names.append(input_name)
    
# print(all_names) 1st way
# for name in all_names:
    # parts = name.split()
    # first_name = parts[0]
    # first_name = first_name.capitalize()
    # full_name = first_name
    # 
    # if len(parts) == 2:
      # last_name = parts[1]
      # last_name = last_name.capitalize()
      # full_name += f" {last_name}"
      # 
    # print(f"{full_name}! you are invited to the party on saturday.")
    
# print(all_names) 2nd way
for name in all_names:
    print(f"{name.title()}! you are invited to the party on saturday.")