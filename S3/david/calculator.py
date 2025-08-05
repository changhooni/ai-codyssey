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

def is_integer_try(x): #정수 여부 확인을 위한 함수
    try:
        int(x)
        return True
    except ValueError:
        return False

def print_result(y): #출력을 위한 함수 지정
    if is_integer_try(y):
        print(f"Result 계산결과 : {y}")
    else:
        print(f"{y}")

# 결과 값 받기
result = 0

#def main():
#    c_num = input('숫자를 입력하세요 : ').split()   
#    operator = input('연산자를 입력하세요 : ')
    #b = int(input('두번째 숫자를 입력하세요 : '))

#    i=0
#    for i in c_num:
#        a = (float(c_num[0])) #c_num애 대한 split 변수값에 첫번째 요소 지정
#        b = (float(c_num[1])) #c_num애 대한 split 변수값에 두번째 요소 지정

#    if operator == '+':
#        result = add(a, b)
#    elif operator == '-':
#        result = subtract(a, b)
#    elif operator == '*':
#        result = multiply(a, b)
#    elif operator == '/':
#        if b == 0:
#            result = 'Error : Division by zero.'
#        else:
#            result = divide(a, b)
#    else:
#        result = 'Invalid operator.'
#    p_result = print_result(result)
    #print(f"Result: {result}")

#def main1():
#    text_num = input('숫자 연산자 숫자 : ').split()

#    result = 0
#    i = 0
#    for i in text_num:
#        a = (float(text_num[0])) #text_num 대한 split 변수값에 첫번째 요소 지정
#        b = (float(text_num[2])) #text_num 대한 split 변수값에 세번째 요소 지정
#        operator = text_num[1] #text_num 대한 split 변수값에 두번째 요소 지정(연산자 확인)
    
#    if operator == "+":
#        result = add(a, b)
#    elif operator == "-":
#        result = subtract(a, b)
#    elif operator == "*":
#        result = multiply(a, b)
#    elif operator == "/":
#        if b == 0:
#            result = 'Error : Division by zero.'
#        else:
#            result = divide(a, b)
#    else:
#        result = 'Invalid operator.'
    #print(f"Result: &lt;계산결과&gt; {result}")
#    p_result = print_result(result)

    # eval() 함수를 사용하여 한줄 연산하기
    #try:
    #    result = eval(operator)
    #    print(f"Result : {result}")
    #except (SyntaxError, NameError):
    #    print("Invalid operator.")
    #except Exception as e:
    #    print("Error :", e)

if __name__ == '__main__':
    select_chk = input("과제 연산식을 선택하세요(1 : 숫자, 연산식, 2 : 숫자 연산식 숫자)")
    if int(select_chk) == 1:
        #main() // 함수로 실행
        c_num = input('숫자를 입력하세요 : ').split()   
        operator = input('연산자를 입력하세요 : ')
        #b = int(input('두번째 숫자를 입력하세요 : '))

        #i=0
        a, b = (int(x) for x in c_num)
        #for i in c_num:
        #    a = (int(c_num[0])) #c_num애 대한 split 변수값에 첫번째 요소 지정
        #    b = (int(c_num[1])) #c_num애 대한 split 변수값에 두번째 요소 지정

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
        p_result = print_result(result)
    elif int(select_chk) == 2:
        #main1() // 함수로 실행
        text_num = input('숫자 연산자 숫자 : ').split()

        a, operator, b = (str(y) for y in text_num)
        a = int(a)
        b = int(b)
        #result = 0
        #i = 0
        #for i in text_num:
        #    a = (int(text_num[0])) #text_num 대한 split 변수값에 첫번째 요소 지정
        #    b = (int(text_num[2])) #text_num 대한 split 변수값에 세번째 요소 지정
        #    operator = text_num[1] #text_num 대한 split 변수값에 두번째 요소 지정(연산자 확인)
            
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
        #print(f"Result: &lt;계산결과&gt; {result}")
        p_result = print_result(result)
    else:
        p_result = print_result("잘못선택하였습니다.")
