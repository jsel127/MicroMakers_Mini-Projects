import random
import time

OPERATOR = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 2



    

def play_game(start_over=True):
    def generate_problem():
        left = random.randint(MIN_OPERAND, MAX_OPERAND)
        right = random.randint(MIN_OPERAND, MAX_OPERAND)
        operator = random.choice(OPERATOR)
        expression = str(left) + " " + str(operator) + " " + str(right)
        answer = eval(expression)
        return expression, answer
    

    input("Press enter to start!")
    print("-" * 40)
    while start_over:
        WRONG_ANSWERS = 0

        start_time = time.time()
        for n in range(TOTAL_PROBLEMS):
            expression, answer = generate_problem()
            while True:
                player_answer = input(f"Problem # {n + 1}: {expression} = ")
                if (player_answer == str(answer)):
                    print("Correct!")
                    break
                print("Wrong. Try again!")
                WRONG_ANSWERS += 1
        end_time = time.time()

        final_score = str(TOTAL_PROBLEMS - WRONG_ANSWERS) + " out of " + str(TOTAL_PROBLEMS) + " (" + str(round((TOTAL_PROBLEMS - WRONG_ANSWERS)/TOTAL_PROBLEMS * 100)) + "%)"
        time_taken = "Time taken: " + str(round(end_time - start_time, 2)) + "seconds"
        print(final_score)
        print(time_taken)
        start_over = input("Try again (Y/N)? ").lower() in ['y', "yes"]
        print("-" * 40)

           
        
# DRIVER
play_game()