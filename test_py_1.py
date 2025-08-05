from flask import Flask

app = Flask(__name__)

def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    if b == 0:
        result = "Error: Division by zero."
    else:
        result = a / b
    return result

def is_int_try(k):
    try:
        int(k)
        return True
    except ValueError:
        return False
    
def result_print(y):
    if is_int_try(y):
        return print(f"Result: <{y}>")
    else:
        return print(y)
    

if __name__ == "__main__":
    select_calculator = input("연산식 방법을 선택 하세요(1-> 숫자 연산식, 2-> 숫자 연산식 숫자)")

    if int(select_calculator) == 1:
        input_num = input("숫자를 입력하세요(공백처리 입력)")
        operator = input("연산자를 등록하세요")

        num = [int(x) for x in input_num.split()]
        a = num[0]
        b = num[1]

        if operator == "+":
            result = add(a, b)
        elif operator == '-':
            result = subtract(a, b)
        elif operator == "*":
            result = multiply(a, b)
        elif operator == "/":
            result = divide(a, b)
        else:
            result = "Invalid operator."
    elif int(select_calculator) == 2:
        input_txt = input("연산식을 등록하세요(숫자 연산식 숫자)").split()

        for x in input_txt:
            a = int(input_txt[0])
            b = int(input_txt[2])
            operator = input_txt[1]

        if operator == "+":
            result = add(a, b)
        elif operator == '-':
            result = subtract(a, b)
        elif operator == "*":
            result = multiply(a, b)
        elif operator == "/":
            result = divide(a, b)
        else:
            result = "Invalid operator."
    else:
        result = "잘못선택하였습니다."

    p_print = result_print(result)