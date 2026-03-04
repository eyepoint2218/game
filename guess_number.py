import random


def play_game() -> None:
    target_number = random.randint(1, 100)
    attempts = 0

    print("숫자 맞추기 게임을 시작합니다!")
    print("1부터 100 사이의 숫자를 맞혀보세요.")

    while True:
        try:
            user_input = input("숫자를 입력하세요: ").strip()
        except EOFError:
            print("\n입력이 종료되어 게임을 종료합니다.")
            break
        except KeyboardInterrupt:
            print("\n게임을 종료합니다.")
            break

        if not user_input.isdigit():
            print("숫자만 입력해주세요.")
            continue

        guess = int(user_input)

        if guess < 1 or guess > 100:
            print("1부터 100 사이의 숫자를 입력해주세요.")
            continue

        attempts += 1

        if guess < target_number:
            print("너무 낮아요!")
        elif guess > target_number:
            print("너무 높아요!")
        else:
            print(f"정답입니다! {attempts}번 만에 맞혔어요.")
            break


if __name__ == "__main__":
    play_game()
