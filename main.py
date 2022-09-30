class Toyota:

    stopped = True

    def __init__(self, model, engine, color):
        self.model = model
        self.engine = engine
        self.color = color

    def description(self):
        print(
            f'Model: {self.model}\nEngine: {self.engine}\nColor: {self.color}')

    def change_color(self):
        new_color = input('Type color would You like: ')

        if new_color != '' and new_color.isalpha():
            self.color = new_color
        else:
            print('You typed wrong color')

    def drive(self):
        self.stopped = False
        print('You are driving!!!')

    def shift_gear(self, up_or_down):
        if self.stopped:
            self.drive()

        if up_or_down == 'up':
            print('Your are driving faster')
        elif up_or_down == 'down':
            print('Your are driving slowly')


my_toyota = Toyota('RAV 4', '2.0 TDI', 'Black')

my_toyota.description()
my_toyota.change_color()
my_toyota.description()

my_toyota.drive()
my_toyota.shift_gir('up')
my_toyota.shift_gir('up')
my_toyota.shift_gir('down')