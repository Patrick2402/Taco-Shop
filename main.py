# taco programming created by Patryk Zawieja CBE/ISA second year of undergraduate studies
import plots
import taco
from addid import add_ingredient
from menu import *
from plots import *
from addid import remove_ingredient
import ingrediens
import admin
def close_app():
    print('Input y if you want to exit: ')
    y = input()
    if y == 'y':
        return False


def Goo():
    main_flag = True
    while main_flag:
        print('WELCOME\n-------------------------------------\n\n')
        interior_flag = True
        person = taco.Taco()
        boss = admin.Person()
        while interior_flag:
            switch()
            Choice = input('\n\nInput choice: ')
            if Choice == '1':
                person.set_new_size()
                add_ingredient(person)
            if Choice == '2':
                person.set_new_size()
            if Choice == '3':
                add_ingredient(person)
            if Choice == '4':
                remove_ingredient(person)
            if Choice == '5':
                name = input('Input your name: ')
                order_file = open(name + '.txt', 'w')
                person.save_your_taco(order_file)
                order_file.close()
                interior_flag = False
            if Choice == '6':
                if not boss.account_is_created:
                    print("Account not created")
                    boss.set_login_and_password()
                    boss.account_is_created = True
                else:
                    if admin.Login(boss):
                        admin.admin_things()

        if not close_app():
            main_flag = False



Goo()
