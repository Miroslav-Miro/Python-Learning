def inventory_showcase(shop):
    for item in shop:
        if item != "name":
            print(f"==[{item}], {shop[item]} gold pieces")

freelancers = {
    "name": "freelancing Shop",
    "brian": 70,
    "black knight": 20,
    "biccus diccus": 100,
    "grim reaper": 500,
    "minstrel": -15,
}
antiques = {
    "name": "Antique Shop",
    "french castle": 400,
    "wooden grail": 3,
    "scythe": 150,
    "catapult": 75,
    "german joke": 5,
}
pet_shop = {"name": "Pet Shop", "blue parrot": 10, "white rabbit": 5, "newt": 2}

player = {"inventory": [], "gold": 1000}
bill = 0

freelancers = {k.lower(): v for k, v in freelancers.items()}

# go in SHOP and buy 1 item
# add itema to player's inventory
for shop in (freelancers, antiques, pet_shop):
    shop_name = shop["name"].title()
    print(f"    Welcome to the: \n ---{shop_name}---")
    print()
    print("We have the following items for sale:")
    print(f"Your inventory: {player['inventory']}")
    inventory_showcase(shop)
    while True:
        picked_item = input("Choose 1 item to buy or type EXIT to leave the shop: ")
        picked_item = picked_item.lower()
        if picked_item == "exit":
            print(f"You exited the {shop_name}")
            print()
            break
        elif picked_item not in shop or picked_item == "name":
            print("Sorry, we do not have that item")
            print()
            inventory_showcase(shop)
        else:
            player["inventory"].append(picked_item)
            player["gold"] -= abs(shop[picked_item])
            bill += abs(shop[picked_item])
            print(f"You purchased {picked_item.upper()} for {shop[picked_item]} gold pieces")
            shop.pop(picked_item)
            break

if len(player["inventory"]) > 0:
    print(f'You purchased the following items: \n{"\n".join(player["inventory"])}')
    print(f"Total cost {bill} gold pieces.")
    print(f"Remaining gold {player['gold']} gold pieces.")
else:
    print("You did not purchase any items")