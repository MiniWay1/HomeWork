# 1. Игровое поле. Создаём его!
field = [' ' for _ in range(9)]
"""
The function creates a field.
"""
# 2. Вывод игрового поля
def field_output(field):
    print(f'{field[0]}  │ {field[1]} │ {field[2]}')
    print('───┼───┼───')
    print(f'{field[3]}  │ {field[4]} │ {field[5]}')
    print('───┼───┼───')
    print(f'{field[6]}  │ {field[7]} │ {field[8]}')

    """
    The function outputs the game board to the console for two players.
    """

# 3. Проверка победителя.
def check_win():
    win_line = ((0,1,2), (3,4,5), (6,7,8), # По горизонтали
                (0,3,6), (1,4,7), (2,5,8), # По вертикали
                (0,4,8), (2,4,6)           # По Диагонали
                )
    for i in win_line:
        if field[i[0]] == field[i[1]] == field[i[2]] and field[i[0]] != ' ':
            return field[i[0]]

    return False # Выносим False за цикл for для работы кода (Проверка победителя).

"""
The function checks who won the game of Tic-Tac-Toe.
"""

#4. Основной цикл игры.
print('Здравствуйте игроки')
def main():
    steps = 0
    win = False
    while not win:
        field_output(field)
        if steps % 2 == 0:
            player = "X"
        else:
            player = "O"

        player_input = input (f"Куда ставим {player}? (1-9): ") # Запросто хода у пользователя.
        try:
            player_input = int(player_input)
        except ValueError:
            print("Ошибка. Введите число от 1 до 9.") # Если пользователь ввёл ни то число.
            continue

        if 1 <= player_input <=9:
            if str(field[player_input-1]) not in "XO": # Строка кода проверяет, содержит ли конкретное поле символ, отличный от крестика ("X") или нолика ("O").
               # Делаем ход.
                field[player_input-1] = player
                steps +=1
            else:
                print("Эта клетка уже занята!")
                continue
        else:
            print("Неверный ввод. ВВедите число от 1 до 9.")
            continue
# Проверка победителя после 4 ходов.
        if steps > 4:
            winner = check_win()
            if winner:
                field_output(field)
                print(f"Игрок {winner} выиграл!")
                win = True
                break
# Проверка на ничью.
        if steps == 9:
            field_output(field)
            print("Ничья!")
            break
"""
The core code for the game's operation.

This code greets the players and prompts each one for a move; if a player makes a mistake when entering a number, the program reports the error and asks for the move again. It also notifies the player if a space is already occupied. Finally, it checks which player has won or whether the game has ended in a draw.
"""
main()