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
a = int(input('첫번째 숫자를 입력하세요 : '))    
operator = input('연산자를 입력하세요 : ')
b = int(input('두번째 숫자를 입력하세요 : '))
# eval() 함수를 사용하여 한줄 연산하기

# 결과 값 받기
result = 0

try:
    result = eval(operator2)
    print(f"Result : {result}")
except (SyntaxError, NameError):
    print("Invalid operator.")
except Exception as e:
    print("Error :", e)

if operator == '+':
    result = add(a, b)
elif operator == '-':
    result = subtract(a, b)
elif operator == '*':
    result = multiply(a, b)
elif operator == '/':
    if b == 0:
        print('Error : Division by zero.')
    else:
        result = divide(a, b)
elif b == 0:
    result = 'Error : Division by zero.'
else:
    result = 'Invalid operator.'
    
def main():
    print(f"Result : {result}")

if __name__ == '__main__':
    main()
