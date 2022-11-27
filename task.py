# Напишите класс TicTacToeBoard для игры в крестики-нолики, который должен иметь следующие методы:
# new_game() – для создания новой игры;
# get_field() – для получения поля (список списков);
# check_field() – для проверки, есть ли победитель, который возвращает X, если победил первый игрок, 0,
# если второй, D, если ничья и None, если можно продолжать игру;
# make_move(row, col) – который устанавливает значение текущего хода в ячейку поля с координатами row, col,
# если это возможно, «переключает» ход игрока, а также возвращает сообщение «Победил игрок X» при победе крестиков,
# «Победил игрок 0» при победе ноликов, «Ничья» в случае ничьей и «Продолжаем играть», если победитель после
# данного хода неопределён.
# Кроме того, метод make_move должен возвращать сообщение «Клетка <row>, <col> уже занята», если в клетке
# уже стоит крестик или нолик, и «Игра уже завершена», если в текущей игре уже выявлен победитель или
# закончились ячейки для ходов.
# При создании объекта класса должна создаваться новая игра.
# Аргументы row и col метода make_move могут принимать значения от 1 до 3.
# Пример:
# board = TicTacToeBoard()
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 1))
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 1))
# print(board.make_move(1, 2))
# print(*board.get_field(), sep="\n")
# print(board.make_move(2, 1))
# print(board.make_move(2, 2))
# print(board.make_move(3, 1))
# print(board.make_move(2, 2))
# print(*board.get_field(), sep="\n")

class TicTacToeBoard:
    winner = 0
    player = 2
    per = ''
    k01 = '-'
    k02 = '-'
    k03 = '-'
    k11 = '-'
    k12 = '-'
    k13 = '-'
    k21 = '-'
    k22 = '-'
    k23 = '-'
    o = ''
    x = ''

    def check(self):
        if self.k01 == 'X' and self.k11 == 'X' and self.k21 == 'X' \
                or self.k02 == 'X' and self.k12 == 'X' and self.k22 == 'X' \
                or self.k03 == 'X' and self.k13 == 'X' and self.k23 == 'X' \
                or self.k01 == 'X' and self.k02 == 'X' and self.k03 == 'X' \
                or self.k11 == 'X' and self.k12 == 'X' and self.k13 == 'X' \
                or self.k21 == 'X' and self.k22 == 'X' and self.k23 == 'X' \
                or self.k01 == 'X' and self.k12 == 'X' and self.k23 == 'X' \
                or self.k03 == 'X' and self.k12 == 'X' and self.k21 == 'X':
            return 'Победил игрок X'
        elif self.k01 == '0' and self.k11 == '0' and self.k21 == '0' \
                or self.k02 == '0' and self.k12 == '0' and self.k22 == '0' \
                or self.k03 == '0' and self.k13 == '0' and self.k23 == '0' \
                or self.k01 == '0' and self.k02 == '0' and self.k03 == '0' \
                or self.k11 == '0' and self.k12 == '0' and self.k13 == '0' \
                or self.k21 == '0' and self.k22 == '0' and self.k23 == '0' \
                or self.k01 == '0' and self.k12 == '0' and self.k23 == '0' \
                or self.k03 == '0' and self.k12 == '0' and self.k21 == '0':
            return 'Победил игрок 0'
        elif self.k01 != '-' and self.k02 != '-' and self.k03 != '-' \
                and self.k11 != '-' and self.k12 != '-' and self.k13 != '-' \
                and self.k21 != '-' and self.k22 != '-' and self.k23 != '-':
            return 'Ничья'
        else:
            return 'Продолжаем играть'

    def row1(self, r1='-', r2='-', r3='-'):
        if self.k01 == '-' and r1 is not None:
            if r1 != '-':
                self.k01 = r1
                return self.check()
            else:
                self.k01 = '-'

        if self.k02 == '-':
            if r2 != '-':
                self.k02 = r2
                return self.check()
            else:
                self.k02 = '-'

        if self.k03 == '-':
            if r3 != '-':
                self.k03 = r3
                return self.check()
            else:
                self.k03 = '-'
        return [self.k01, self.k02, self.k03]

    def row2(self, r1='-', r2='-', r3='-'):
        if self.k11 == '-' and r1 is not None:
            if r1 != '-':
                self.k11 = r1
                return self.check()
            else:
                self.k11 = '-'

        if self.k12 == '-':
            if r2 != '-':
                self.k12 = r2
                return self.check()
            else:
                self.k12 = '-'

        if self.k13 == '-':
            if r3 != '-':
                self.k13 = r3
                return self.check()
            else:
                self.k13 = '-'

        return [self.k11, self.k12, self.k13]

    def row3(self, r1='-', r2='-', r3='-'):
        if self.k21 == '-':
            if r1 != '-' and r1 is not None:
                self.k21 = r1
                return self.check()
            else:
                self.k21 = '-'

        if self.k22 == '-':
            if r2 != '-' and r2 is not None:
                self.k22 = r2
                return self.check()
            else:
                self.k22 = '-'

        if self.k23 == '-':
            if r3 != '-':
                self.k23 = r3
                return self.check()
            else:
                self.k23 = '-'
        return [self.k21, self.k22, self.k23]

    def new_game(self):
        self.winner = 0
        self.player = 2
        self.per = '-'
        self.k01 = '-'
        self.k02 = '-'
        self.k03 = '-'
        self.k11 = '-'
        self.k12 = '-'
        self.k13 = '-'
        self.k21 = '-'
        self.k22 = '-'
        self.k23 = '-'
        self.o = ''
        self.x = ''

    def get_field(self):
        return self.row1(), self.row2(), self.row3()

    def check_winner(self, s):
        if s == 'Победил игрок X':
            self.winner += 1
            self.x = 1
            return 'Победил игрок X'
        elif s == 'Победил игрок 0':
            self.winner += 1
            self.o = 1
            return 'Победил игрок 0'
        elif s == "Ничья":
            self.winner -= 1
            return 'Ничья'
        else:
            return 'Продолжаем играть'

    def check_field(self):
        if self.x == 1:
            return 'X'
        elif self.o == 1:
            return '0'
        elif self.winner == -1:
            return 'D'
        else:
            return None

    def make_move(self, row, col):
        if self.winner == 0:
            if self.player == 2:
                self.per = 'X'
                self.player += 1
            else:
                self.per = '0'
                self.player -= 1
            
            if row == 1:
                if col == 1 and self.k01 == '-':
                    s = self.row1(self.per)
                    return self.check_winner(s)
                elif col == 2 and self.k02 == '-':
                    s = self.row1(None, self.per)
                    return self.check_winner(s)
                elif col == 3 and self.k03 == '-':
                    s = self.row1(None, None, self.per)
                    return self.check_winner(s)
                else:
                    if self.player == 3:
                        self.player -= 1
                    else:
                        self.player += 1
                    return 'Клетка ' + str(row) + ', ' + str(col) + ' уже занята'
            elif row == 2:
                if col == 1 and self.k11 == '-':
                    s = self.row2(self.per)
                    return self.check_winner(s)
                elif col == 2 and self.k12 == '-':
                    s = self.row2(None, self.per)
                    return self.check_winner(s)
                elif col == 3 and self.k13 == '-':
                    s = self.row2(None, None, self.per)
                    return self.check_winner(s)
                else:
                    if self.player == 3:
                        self.player -= 1
                    else:
                        self.player += 1
                    return 'Клетка ' + str(row) + ', ' + str(col) + ' уже занята'
            elif row == 3:
                if col == 1 and self.k21 == '-':
                    s = self.row3(self.per)
                    return self.check_winner(s)
                elif col == 2 and self.k22 == '-':
                    s = self.row3(None, self.per)
                    return self.check_winner(s)
                elif col == 3 and self.k23 == '-':
                    s = self.row3(None, None, self.per)
                    return self.check_winner(s)
                else:
                    if self.player == 3:
                        self.player -= 1
                    else:
                        self.player += 1
                    return 'Клетка ' + str(row) + ', ' + str(col) + ' уже занята'
        else:
            return 'Игра уже завершена'


board = TicTacToeBoard()
print(*board.get_field(), sep='\n')
print(board.make_move(1, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 2))
print(board.make_move(3, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 2))
print(*board.get_field(), sep="\n")