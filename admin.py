import re
from plots import Show_plot


class Person:
    password = object
    login = object
    account_is_created = False

    def __init__(self, name='Admin'):
        self.name = name

    def ShowData(self):
        print(f"Name: {self.name}")

    def set_login_and_password(self):
        try:
            self.set_password()
            self.login = input("Input new login: ")
            # 6self.account_is_created = True
        except SystemError:
            print("Something went wrong")

    def set_password(self):
        p_one = "^[A-Z]"
        p_two = "[a-z]"
        p_three = "[0-9]"
        p_four = "\W"
        p_five = ".{6}"
        flag = True
        while flag:
            self.password = input('Input new password: ')
            if re.findall(p_one, self.password) and re.findall(p_two, self.password) and re.findall(p_three,
                                                                                                    self.password) and re.findall(
                p_four, self.password) and re.findall(p_five, self.password):
                print('correct')
                flag = False
            else:
                print('no no no, try again ')


# end of class Person


def Login(boss):
    # if not boss.account_is_created:
    # print("Account not created")
    # boss.set_login_and_password()
    # boss.account_is_created = True
    # return
    # else:
    count = 0
    while count < 3:
        login = input("Input login: ")
        password = input("Input password: ")
        if login == boss.login and password == boss.password:
            print("Logged")
            return True
            break
        else:
            if count == 3:
                print('Account locked')
                return False
                break
            else:
                count = count + 1
                print("Wrong login or password, try again")
                continue

def admin_things():
    Show_plot()