MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        lines = input("Enter the number of lines to bet on (1- " + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
        
    return lines



def get_number_of_lines():
    