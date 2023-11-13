import random


def random_integer(min_value, max_value):
    """
    Function generates a random integer with in the range.

    Parameters:
    - min_value (int): The minimum value of the range.
    - max_value (int): The maximum value of the range.

    Returns:
    int: A random integer within the range.
    """
    return random.randint(min_value, max_value)


def random_operator():
    """
    Function chooses a random mathematical operator from the list.

    Returns:
    str: A randomly chosen mathematical operator.
    """
    return random.choice(['+', '-', '*'])


def math_problem(num1, num2, operator):
    """
    Function Generates a math problem and calculate the answer.

    Parameters:
    - num1 (float): The first operand.
    - num2 (float): The second operand.
    - operator (str): The mathematical operator.

    Returns:
     the math problem as a string and the answer.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer


def math_quiz():
    """
    Main function to conduct the Math Quiz.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for q_num in range(1, total_questions+1):
        num1 = random_integer(1, 10)
        num2 = random_integer(1,int(5.5))
        operator = random_operator()

        problem, answer = math_problem(num1, num2, operator)
        print(f"\nQuestion {q_num}: {problem}")
        user_answer = input("Your answer: ")
        while True:  # Error Handling
            user_answer = input("Your answer: ")
            try:
                user_answer = float(user_answer)
                break  # Exit the loop if conversion is successful
            except ValueError:
                print("your input is Invalid. Please enter a number.")
              

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
