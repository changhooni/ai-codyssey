from flask import Flask

app = Flask(__name__)

def is_integer_try(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def main():
    try:
        #print(f'{power_number}')
        #print(f'{input_number}')
        #def power(base, exponent):
        input_number = int(input('제곱을 구할 값을 입력하세요 : '))
        power_number = input('몇 제곱 값을 입력하세요 : ')

        if is_integer_try(power_number):
            #print(input_number, '의', power_number, '제곱 = ', math.pow(input_number, power_number)) # math.pow() 함수를 사용하여 처리 방법
            #squared_number = power(input_number, power_number)
            result = 1
            # for문에 _는 변수 값이 필요 없을 때 사용한다
            for _ in range(int(power_number)):
                #print(f'squared_number1 : {result}')
                result *= int(input_number)
            print(f'Result : {result}')
        else:            
            print("Invalid exponent input.")
        #result = eval(operator2)
        #print(f"Result : {result}")
    except Exception as e:
        print("Invalid number input.")


#input_number = int(input('제곱을 구할 값을 입력하세요 : '))
#power_number = int(input('몇 제곱 값을 입력하세요 : '))
#s_number = s_number(input_number, power_number)
#squared_number = power(input_number, power_number)


if __name__ == "__main__":
    main()