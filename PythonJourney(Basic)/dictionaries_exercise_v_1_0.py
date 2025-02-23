freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}
player = {'inventory':[]}

freelancers = {k.lower(): v for k, v in freelancers.items()}

# Print out the name of each shop and the items they sell
for shop in (freelancers, antiques, pet_shop):
    print(f'    Welcome to the: \n ---{shop['name']}---')
    print()
    print('We have the following items for sale:')
    
    while True:
     for item in shop:
        if item != 'name':
            print(f'==[{item}], {shop[item]} gold pieces')
     picked_item = input("Choose 1 item to buy: ")
     picked_item = picked_item.lower()
     if picked_item not in shop:
         print('Sorry, we do not have that item')
         break
     else:
        break
        
    player['inventory'].append(picked_item)
    print(f'You purchased {picked_item} for {shop[picked_item]} gold pieces')
    shop.pop(picked_item) 

print(f'You purchased the following items:{"".join(player["inventory"])}')


    

    


    
    

    


    



    






            
            