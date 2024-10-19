def main():
    cal = {
            "+" : add,
            "-" : subtract,
            "*" : multiply,
            "/" : divide
        }
    calculator(cal)
    

def calculator(cal):
    a = float(input("Enter the first number: "))
    for symbol in cal:
        print(symbol)
    while (True):
        operator = input("Enter the operator: ")
        if operator not in cal:
            print("Invalid operator:")
            continue
        b = float(input("Enter the next number: "))
        answer = cal[operator](a,b)
        print(f"{a} {operator} {b} = {answer}")
        if answer !="zero division error":
            again = input(f"type 'y' to continue with {answer} or type n for new calculation or any other letter to end calculation: ").lower()
            if again == 'y':
                a = answer
            elif again == 'n':
                main()
            else:
                break
        else:
            again = input(f"type 'y' for new calculation or type anything to exit: ").lower()
            if again == 'y':
                main()
            else:
                break


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1 , n2):
    return n1*n2
def divide(n1 , n2):
    if n2 == 0:
        return "zero division error"
    return n1 / n2


if __name__ == "__main__":
    main()