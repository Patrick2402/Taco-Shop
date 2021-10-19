import ingrediens


def exit():  # basic exit function, if u press N -> exit
    exit_key = input()
    if exit_key == 'n':
        return True


def add_ingredient(tacos):  # adding ingredients to your taco
    while 1:
        print('List of ingredients')
        for ing, price in ingrediens.dict_of_ingrediens.items():
            print(ing, price, end="; ")
        items_to_add = input('\nWhat do u want to add?\n'
                             'I want to add: ')
        if items_to_add not in ingrediens.dict_of_ingrediens:
            print('Not existing ingredient at the list')
        else:
            if items_to_add not in tacos.list_of_ingrediens:
                tacos.list_of_ingrediens.append(items_to_add)
                tacos.price = tacos.price + ingrediens.dict_of_ingrediens[items_to_add]
                print('You added ' + items_to_add)
                print('Do u want to exit?'
                      '\nPress y if yes or n if no ')
                if not exit():
                    break
            else:
                print("Ups you had added this ingredient before")


def remove_ingredient(tacos):
    print('Which ingredient do you want to remove?')
    name_of_ingredient = input('My choice: ') # var of removing ingredient
    if name_of_ingredient in tacos.list_of_ingrediens: # if ingredient is in taco remove from the list
        tacos.list_of_ingrediens.remove(name_of_ingredient)
        tacos.price = tacos.price - ingrediens.dict_of_ingrediens[name_of_ingredient]
        print('You removed a ingredient')
    else:
        print('No ingredient in your taco')
