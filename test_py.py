from flask import Flask

app = Flask(__name__)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero."
    else:
        return a / b
    
def is_int_try(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def result_msg(y):
    if is_int_try(y):
        print(f"Result : {y}")
    else:
        print(f"{y}")

def main():
    input_text = input("숫자를 입력하세요")
    operator = input("연산자를 등록하세요")
    
    #if is_int_try(input_text):
    
    num = [int(x) for x in input_text.split()]
    i = 0
    k = len(num)
    if operator == "+" or operator == "-":
        result = 0
    elif operator == "*" or operator == "/":
        result = 1
    else:
        result = "Invalid operator"

    while i < k:
        if operator == "+":
            result += num[i]
        elif operator == "-":
            result =- num[i]
        elif operator == "*":
            result *= num[i]
        elif operator == "/":
            if num[i] == 0:
                result = "Error: Division by zero."
                break
            else:
                result /= num[i]
        else:
            result = "Invalid operator." 
        i += 1

    result_msg(result)        

    a = num[0]
    b = num[1]

    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = subtract(a, b)
    elif operator == "*":
        result = multiply(a, b)
    elif operator == "/":
        result = divide(a, b)
    else:
        result = "Invalid operator."
        
    result_msg(result)
        
if __name__ == "__main__":
    main()
        


