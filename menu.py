

class Menu:
    def __init__(self, title, algorithms):
        self.Title = title
        self.Algorithms = algorithms

    def Run(self):
        self.DisplayMenu()

    def DisplayMenu(self):
        print('#'*40)
        print('# {:<36} #'.format(self.Title))
        print('#'*40)
        for i in range(0, 13):
            print('#' + ' '*38 + '#')
        print('#'*40)
