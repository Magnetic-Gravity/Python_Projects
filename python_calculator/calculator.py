HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE, "r")
    lines = file.readlines()
    if len(lines)==0:
        print("No history available.")
    else:
        for line in lines:
            print(line.strip()) #removes leading and trailing whitespace (spaces, tabs, newlines)
    file.close()
    
def clear_history():
    file = open(HISTORY_FILE, "w")
    file.close()
    print("History cleared.")

def save_to_history(equation, result):
    file = open(HISTORY_FILE, "a")
    file.write(equation + " = " + str(result) + "\n")
    file.close()
    
def calculate(user_input):
    parts = user_input.split()
    if len(parts) !=3:
        print("Error: Invalid input format. Use format: number operator number")
        return 
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Error: Division by zero not allowed.")
            return
        result = num1 / num2
    else:
        print("Error: Invalid operator. USE ONLY +, -, *, /")
        return
        
    if int(result) == result:
        result = int(result)
    print(f"Result :", result)
    save_to_history(user_input, result)
    
def main():
    print('---Welcome to the Simple PYTHON CALCULATOR (type history, clear or exit)')
    while True:
        user_input = input("Enter calculation (+ - * /) or command (history, clear or exit) ")
        if user_input.lower() == "exit":
            print("Exiting calculator. GOODBYE!")
            break
        elif user_input.lower() == "history":
            show_history()
        elif user_input.lower() == "clear":
            clear_history()
        else:
            calculate(user_input)

main()
