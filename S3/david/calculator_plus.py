from flask import Flask

app = Flask(__name__)

def add(a, b):
    return a + b
 
def subtract(a, b):
    return a - b
 
def multiply(a, b):
    return a * b
 
def divide(a, b):
    return a / b

text_num = input('연산식을 입력하세요 : ').split()

def main():
    result = 0
    i = 0
    for i in text_num:
        a = int(float(text_num[0]))
        b = int(float(text_num[2]))
        operator = text_num[1]
    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = subtract(a, b)
    elif operator == "*":
        result = multiply(a, b)
    elif operator == "/":
        if b == 0:
            result = 'Error : Division by zero.'
        else:
            result = divide(a, b)
    else:
        result = 'Invalid operator.'
    print(f"Result : {result}")

    # eval() 함수를 사용하여 한줄 연산하기
    #try:
    #    result = eval(operator)
    #    print(f"Result : {result}")
    #except (SyntaxError, NameError):
    #    print("Invalid operator.")
    #except Exception as e:
    #    print("Error :", e)


if __name__ == '__main__':
    main()
