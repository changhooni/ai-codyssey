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

c_num = input('숫자를 입력하세요 : ').split()   
operator = input('연산자를 입력하세요 : ')
#b = int(input('두번째 숫자를 입력하세요 : '))

# 결과 값 받기
result = 0

def main():
    i=0
    for i in c_num:
        a = int(float(c_num[0])) #c_num애 대한 split 변수값에 첫번째 요소 지정
        b = int(float(c_num[1])) #c_num애 대한 split 변수값에 두번째 요소 지정

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = subtract(a, b)
    elif operator == '*':
        result = multiply(a, b)
    elif operator == '/':
        if b == 0:
            result = 'Error : Division by zero.'
        else:
            result = divide(a, b)
    else:
        result = 'Invalid operator.'
    print(f"Result : {result}")

text_num = input('연산식을 입력하세요 : ').split()

def main1():
    result = 0
    i = 0
    for i in text_num:
        a = int(float(text_num[0])) #text_num 대한 split 변수값에 첫번째 요소 지정
        b = int(float(text_num[2])) #text_num 대한 split 변수값에 세번째 요소 지정
        operator = text_num[1] #text_num 대한 split 변수값에 두번째 요소 지정(연산자 확인)
    
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
    main1()
