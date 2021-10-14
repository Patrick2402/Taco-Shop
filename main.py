# taco programming created by Patryk Zawieja CBE/ISA second year of undergraduate studies
import taco
from addid import add_ingredient
from addid import remove_ingredient
import ingrediens


def foo():
    name = input('Input name of user: ')
    name = taco.Taco()
    name.set_new_size()
    add_ingredient(name)
    remove_ingredient(name)
    name.show_all_ingrediens()
    print(name.size)



foo()
