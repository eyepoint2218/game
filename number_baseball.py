import random


def generate_answer(length: int = 3) -> str:
    """중복되지 않는 숫자 정답을 생성합니다."""
    digits = random.sample("0123456789", length)
    if digits[0] == "0":
        swap_index = next((i for i, d in enumerate(digits) if d != "0"), 1)
        digits[0], digits[swap_index] = digits[swap_index], digits[0]
    return "".join(digits)


def validate_guess(guess: str, length: int = 3) -> bool:
    """입력값이 게임 규칙에 맞는지 확인합니다."""
    return (
        len(guess) == length
        and guess.isdigit()
        and len(set(guess)) == length
        and guess[0] != "0"
    )


def count_strike_ball(answer: str, guess: str) -> tuple[int, int]:
    """스트라이크와 볼 개수를 계산합니다."""
    strike = sum(a == g for a, g in zip(answer, guess))
    ball = sum((digit in answer) for digit in guess) - strike
    return strike, ball


def play_game() -> None:
    """숫자 야구 게임을 실행합니다."""
    print("=== 숫자 야구 게임 ===")
    print("서로 다른 3자리 숫자를 맞혀보세요. (첫 자리는 0 불가)")
    print("종료하려면 'q' 또는 'quit' 입력")

    answer = generate_answer(3)
    attempts = 0

    while True:
        guess = input("\n숫자를 입력하세요: ").strip().lower()

        if guess in {"q", "quit"}:
            print(f"게임을 종료합니다. 정답은 {answer}였습니다.")
            break

        if not validate_guess(guess, 3):
            print("입력 오류: 중복 없는 3자리 숫자를 입력하세요. (예: 583)")
            continue

        attempts += 1
        strike, ball = count_strike_ball(answer, guess)

        if strike == 3:
            print(f"정답! {attempts}번 만에 맞췄습니다 🎉")
            break

        if strike == 0 and ball == 0:
            print("아웃! (0스트라이크 0볼)")
        else:
            print(f"{strike}스트라이크 {ball}볼")


if __name__ == "__main__":
    play_game()
