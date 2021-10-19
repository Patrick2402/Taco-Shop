import self


def how_many_which_sizes():
    print(f'Small sizes: {Taco.how_many_small_one}')
    print(f'Medium sizes: {Taco.how_many_medium_one}')
    print(f'Large sizes: {Taco.how_many_large_one}')


class Taco:
    how_many_small_one = 4  # three static vars
    how_many_medium_one = 5
    how_many_large_one = 8
    list_of_ingrediens = []  # empty list of ingredients
    price = 0  # price
    size = ''  # size

    def set_new_size(self):  # setting new size
        list_of_sizes = ['small', 'medium', 'large']  # list of sizes
        print('Available sizes')
        print('small,medium,large')
        while True:  # infinity loop
            new_size_of_taco = input("Pleate input new size of taco: ")  # variable str

            if new_size_of_taco not in list_of_sizes:
                print('Ops, something went wrong, try again')
            else:
                self.size = new_size_of_taco  # setting new size
                if new_size_of_taco == 'small':
                    Taco.how_many_small_one += 1
                elif new_size_of_taco == 'medium':
                    Taco.how_many_medium_one += 1
                else:
                    Taco.how_many_large_one += 1
                print('You changed tacos size')
                break

    def show_all_ingrediens(self):
        print("Size: " + self.size)  # size
        for items in self.list_of_ingrediens:  # ingredients
            print(items, end=" ")
        print('\nPrice: ', self.price, '$')  # price

    def save_your_taco(self,order_file):
        self.price = round(self.price, 3)
        order_file.write("Its your taco\n")
        order_file.write('Size: ' + self.size + '\n')
        order_file.write(f'Price: {self.price} $\n')
        order_file.write(f'Ingredients: {self.list_of_ingrediens}')
