# Задача 4. Крестики-нолики

# Напишите программу, которая реализует игру Крестики-нолики. 

# Ваши классы в этой задаче могут выглядеть так:

# class Cell:
#    #  Клетка, у которой есть значения
#    #   - занята она или нет
#    #   - номер клетки

# class Board:
#    #  Класс поля, который создаёт у себя экземпляры клетки

# class Player:
#    #  У игрока может быть
#    #   - имя
#    #   - на какую клетку ходит

class Cell:
    def __init__(self, number):
        self.number = number
        self.mark = " "
    def __str__(self):
        return self.mark

class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(9)]
    
    def terminal_board(self):
        for i in range(0, 9, 3):
            print(" ".join([str(cell) for cell in self.cells[i:i+3]]))
            if i!= 9:
                print("- " * 3)

class Player:
    def __init__(self, name):
        self.name = name
        self.cell = None
        self.mark = " X " if self.name == "Игрок" else " O "
    
    def __str__(self):
        return f"{self.name} ({self.mark})"
        
class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("X"), Player("O")]
        self.player = self.players[0]
    
   
    def play(self):
        while True:
            self.board.terminal_board()
            self.player.cell = int(input("Номер клетки: ")) - 1
            self.board.cells[self.player.cell].mark = self.player.name
            self.switch()
    
    def switch(self):
        self.player = self.players[self.players.index(self.player) ^ 1]

    def game(self):
        for i in range(0, 9, 3):
            if self.board.cells[i:i+3].count(self.board.cells[i].mark) == 3:
                return True
        for i in range(3):
            if self.board.cells[i::3].count(self.board.cells[i].mark) == 3:
                return True
        if self.board.cells[0].mark == self.board.cells[4].mark == self.board.cells[8].mark == self.board.cells[0].mark:
            return True
        if self.board.cells[2].mark == self.board.cells[4].mark == self.board.cells[6].mark == self.board.cells[2].mark:
            return True
        return False
    
    def draw(self):
        return self.board.cells.count("") == 0
    
game = Game()

game.play()

# # При первом запуске может быть ошибка, но при повторном запуске работает.
# line 81, in <module>
# line 56, in play