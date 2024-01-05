import random
import time


def math_generator():
    operators = ["+", "-", "//", "%"]

    left = random.randint(25, 40)
    right = random.randint(1, 10)

    question = f"{left} {random.choice(operators)} {right}"
    answer = eval(question)

    problem = f"{question} = "

    return [problem, answer]


def main():
    print("Welcome to math game!")

    if (
        input("Are you ready to play? (y)\nTimer starts when you type y: ").lower()
        == "y"
    ):
        start_time = time.time()
        print("")

        total_challenges = 10
        for id in range(total_challenges):
            print(f"Problem {id+1}")
            challenge, answer = math_generator()

            while True:
                user_input = input(f"{challenge}")
                if user_input.isdigit() and int(user_input) == answer:
                    print("Correct!")
                    break
                elif user_input.isdigit() and int(user_input) != answer:
                    print("Try again!")
                else:
                    print("Please enter a number!")

            print("")

        end_time = time.time()
        duration = end_time - start_time
        print(f"Well done! Finished in {round(duration, 2)} seconds")

    else:
        print("Goodbye!")


if __name__ == "__main__":
    main()
    print("")
