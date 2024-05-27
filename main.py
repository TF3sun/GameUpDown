import random
import json

def main():
    print('업다운 게임을 실행합니다.')

    while True:
        input_num = int(input('옵션을 선택하세요\n1.게임시작\n>>> '))

        if check_user_input(input_num, 'main_menu') == True:
            break
        else:
            print('올바른 입력이 아닙니다.')

    select_main_menu(input_num)

            

def check_user_input(input, option):
    match option:
        case 'main_menu':
            if input in [1]:
                return True
            else:
                return False

def select_main_menu(input_num):
    match input_num:
        case 1:
            play_game()

    return

def play_game():
    rand_num = random.randint(1,100)
    chance = 5

    while chance > 0:
        input_num = int(input(f'수를 입력하세요 기회 {chance}번\n>>> '))

        if rand_num > input_num:
            print(f'{input_num}보다 큽니다')
        elif rand_num < input_num:
            print(f'{input_num}보다 작습니다')
        else:
            print('정답입니다!')
            return
            
        chance -= 1

        if chance == 0:
            print(f'실패입니다 정답은 {rand_num}')
            return

while True:
    main()