import matplotlib.pyplot as plt
from taco import Taco


def Show_plot(): # function which showing plot: number of individual size
    print('It is your plot called "number of individual sizes"')
    y_aside = [Taco.how_many_small_one, Taco.how_many_medium_one, Taco.how_many_large_one]
    x_aside = ['small', 'medium', 'large']
    plt.bar(x_aside, y_aside, color='green', width=0.5)
    plt.grid(color='black', axis='y', linewidth=0.2)
    plt.title('number of individual sizes')
    plt.show()
