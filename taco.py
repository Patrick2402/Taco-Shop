class Taco:
    list_of_ingrediens = []
    price = 0
    size = ''
    #def __init__(self, size):
      #  self.size = size

    def set_new_size(self):
        list_of_sizes = ['small', 'medium', 'large']
        print('Available sizes')
        print('small,medium,large')
        while True:
            new_size_of_taco = input("Pleate input new size of taco: ")
            if new_size_of_taco not in list_of_sizes:
                print('Ops, something went wrong, try again')
            else:
                self.size = new_size_of_taco
                print('You changed tacos size')
                break

    def show_all_ingrediens(self):
        print("Size: " + self.size)
        for items in self.list_of_ingrediens:
            print(items, end=" ")
            # showing price
        print('Price: ', self.price, '$')

