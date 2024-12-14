import random
import time
import threading

def get_time_limit():
    while True:
        try:
            time_limit = float(input("Set Time Limit (in seconds): "))
            return time_limit
        except ValueError:
            print("Invalid input. Please enter a number.")

print("Welcome to the math game!")
time_limit = get_time_limit()
print(f"Time Limit Set to: {time_limit} seconds")

score = 0
operations = ["+", "-", "*", "/"]
total_time = 0
question_count = 0
timeout = False

def time_up():
    global timeout
    timeout = True
    print("\nTime's Up! No more questions. (enter anything to view your results)")


timer_thread = threading.Timer(time_limit, time_up)
timer_thread.start()

while not timeout:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(operations)
    question = f"What is {num1} {operation} {num2}?: "

    if operation == "/" and num2 == 0:
        continue

    
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation == "*":
        answer = num1 * num2
    elif operation == "/":
        answer = round(num1 / num2, 1)


    if timeout:
        break

    
    start_time = time.time()
    
    
    user_answer = None
    try:
        user_answer = float(input(question)) 
    except ValueError:
        print("Invalid input. Please enter a number.")
    
    end_time = time.time()
    
    if timeout: 
        break

    elapsed_time = end_time - start_time
    total_time += elapsed_time
    question_count += 1

    if user_answer == answer:
        score += 1
        print(f"Correct! Current score: {score}")
    else:
        score -= 1
        print(f"Wrong! The correct answer was {answer}.")
    
    print("*" * 20)


timer_thread.cancel()


print(f"Game Over! Final Score: {score}")
if question_count > 0:
    average_time = total_time / question_count
    print(f"Average time per question: {average_time:.2f} seconds")
else:
    print("No questions answered.")
