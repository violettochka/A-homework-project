class PlaceOfFigureExeption(Exception):
    pass


place_letter =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
place_numner =[1, 2, 3, 4, 5, 6, 7, 8]


class Color():
    BLACK = 'black'
    WHITE = 'white'


class Figure():

    def __init__(self, name,  color, place_of_number, place_of_letter):
        self.color = color
        self.name = name
        self.validate_number(place_of_number)
        self.place_of_number = place_of_number
        self.validate_letter(place_of_letter)
        self.place_of_letter = place_of_letter

    def __str__(self):
        return(f'Your figure is {self.name} and has a {self.color} color. Your position is {self.place_of_letter}{self.place_of_number}')

    def validate_letter(self, letter):
        if letter not in place_letter:
            raise PlaceOfFigureExeption('You should change position!') 

    def validate_number(self, number):
        if number not in place_numner:
            raise PlaceOfFigureExeption('You should change position!')

    def change_color(self):
        if self.color == 'white':
            self.color = 'black'
        elif self.color == 'black':
            self.color = 'white' 
        return f'your new color is {self.color}'

    def change_place(self, new_place_number, new_place_letter):
        self.validate_number(new_place_number)
        self.place_of_number = new_place_number
        self.validate_letter(new_place_letter)
        self.place_of_letter = new_place_letter
        return f"your new place is {self.place_of_letter}{self.place_of_number}"


class Pawn(Figure):
    #описание класса для пешки
    def move(self, number, letter):
        self.validate_number(number)
        self.validate_letter(letter)
        #первый способ походить пешкой - это ход в начале игры на две клетки вперед(counter_move = 0)
        if number == (self.place_of_number + 2)and counter_move == 0 and letter == self.place_of_letter:
            self.place_of_number = number
            self.place_of_letter = letter
        #второй способ походить пешкой - все следующие ходы на одну клетку вперед
        elif number == (self.place_of_number + 1) and letter == self.place_of_letter:
            self.place_of_number = number
            self.place_of_letter = letter   
        #третий способ походить пешкой - забрать чужую фигуру, походив на одну клетку по диагонали      
        elif number == (self.place_of_number + 1) and (place_letter.index(letter) == place_letter.index(self.place_of_letter)+ 1 or place_letter.index(letter) == place_letter.index(self.place_of_letter) - 1) :
            self.place_of_number = number
            self.place_of_letter = letter    
        else:
            return f'you cant move your pawn in this way\n'    

        return f'you had a move. Your new position is {self.place_of_letter}{self.place_of_number}\n'    


class King(Figure):
    #описание класса для короля
    def move(self, number, letter):
        self.validate_number(number)
        self.validate_letter(letter)
    #движение на одну клетку вперед или назад
        if number == (self.place_of_number + 1) or number == (self.place_of_number - 1) and letter == self.place_of_letter:
            self.place_of_number = number
            self.place_of_letter = letter 
    #движение на одну клетку вправо или влево
        elif number == self.place_of_number and (place_letter.index(letter) == place_letter.index(self.place_of_letter)+ 1 or place_letter.index(letter) == place_letter.index(self.place_of_letter) - 1):
            self.place_of_number = number
            self.place_of_letter = letter 
    #движение на одну клетку вперед по диагонали 
        elif number == (self.place_of_number + 1) and (place_letter.index(letter) == place_letter.index(self.place_of_letter)+ 1 or place_letter.index(letter) == place_letter.index(self.place_of_letter) - 1) :
            self.place_of_number = number
            self.place_of_letter = letter      
    #движение на одну клетку назад по диагонали
        elif number == (self.place_of_number - 1) and (place_letter.index(letter) == place_letter.index(self.place_of_letter)+ 1 or place_letter.index(letter) == place_letter.index(self.place_of_letter) - 1) :
            self.place_of_number = number
            self.place_of_letter = letter
        else:
            return f'you cant move your king in this way\n'    

        return f'you had a move. Your new position is {self.place_of_letter}{self.place_of_number}\n' 


class Queen(Figure):
    #описание класса для ферзя
    #движение ферзя возможно на любую клетку поля
    def move(self, number, letter):
        self.validate_number(number)
        self.validate_letter(letter)
        self.place_of_number = number
        self.place_of_letter = letter
        return f'you had a move. Your new position is {self.place_of_letter}{self.place_of_number}\n'    
    

class Rook(Figure):
    #описание класса для ладьи
    def move(self, number, letter):
        self.validate_number(number)
        self.validate_letter(letter) 
        #движение по горизонтали
        if number == self.place_of_number and letter != self.place_of_letter:
            self.place_of_number = number
            self.place_of_letter = letter
        #движение по вертикали
        elif number != self.place_of_number and letter == self.place_of_letter:
            self.place_of_number = number
            self.place_of_letter = letter
        else:
            return f'you cant move your rook in this way\n'

        return f'you had a move. Your new position is {self.place_of_letter}{self.place_of_number}\n'    


class Elephant(Figure):
    #описание класса для слона
    def move(self, number, letter):
        self.validate_number(number)
        self.validate_letter(letter) 
        #движение по правой диагонали
        if number != self.place_of_number and letter != self.place_of_letter and self.place_of_number - number ==  place_letter.index(letter) - place_letter.index(self.place_of_letter) :
            self.place_of_number = number
            self.place_of_letter = letter
        #движение по левой диагонали
        elif number != self.place_of_number and letter != self.place_of_letter and self.place_of_number - number ==  place_letter.index(self.place_of_letter) - place_letter.index(letter) :
            self.place_of_number = number
            self.place_of_letter = letter    
        else:
            return f'you cant move your elephant in this way\n'

        return f'you had a move. Your new position is {self.place_of_letter}{self.place_of_number}\n'
    


class Horse(Figure):
    #описание класса для коня
    def move(self, number, letter):
        self.validate_number(number)
        self.validate_letter(letter)
        #движение буквой г в право или влево
        if number == self.place_of_number + 2 and (place_letter.index(letter) == place_letter.index(self.place_of_letter)+ 1 or place_letter.index(letter) == place_letter.index(self.place_of_letter) - 1):
            self.place_of_number = number
            self.place_of_letter = letter
        else:
            return f'you cant move your horse in this way\n'

        return f'you had a move. Your new position is {self.place_of_letter}{self.place_of_number}\n'


pawn1 = Pawn('Pawn', Color.WHITE, 2, 'H')
print(pawn1)
print(pawn1.move(3, 'H'))

king1 = King("King", Color.WHITE, 3, 'B')
print(king1)
print(king1.move(4, 'A'))

queen1 = Queen("Queen", Color.BLACK, 4, 'C')
print(queen1)
print(queen1.move(8, 'E'))

rook1 = Rook('Rook', Color.WHITE, 1, "A")
print(rook1)
print(rook1.move(1, 'G'))

elephant1 = Elephant('Elephant', Color.WHITE, 5, 'F')
print(elephant1)
print(elephant1.move(1, 'B'))

horse1 = Horse('Horse', Color.WHITE, 4, 'E')
print(horse1)
print(horse1.move(6, "F"))

list_of_figure = [pawn1, king1, queen1, rook1, elephant1, horse1]

def achieve_field(list_, number, letter):
    result = []
    for element in list_:
        if f'{letter}{number}' in element.move(number, letter):
            result.append(element.__class__.__name__)
    return result

print(achieve_field([pawn1, king1, queen1, rook1, elephant1, horse1], 4, 'H'))