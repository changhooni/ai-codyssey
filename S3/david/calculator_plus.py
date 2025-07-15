from flask import Flask

app = Flask(__name__)

def add(a, b):
    return a + b
 
def subtract(x, b):
    return a - b
 
def multiply(a, b):
    return a * b
 
def divide(a, b):
    return a / b

operator2 = input('계산할 숫자를 입력하세요 : ')

def main():
    # eval() 함수를 사용하여 한줄 연산하기
    try:
        result = eval(operator2)
        print(f"Result : {result}")
    except (SyntaxError, NameError):
        print("Invalid operator.")
    except Exception as e:
        print("Error :", e)


if __name__ == '__main__':
    main()
