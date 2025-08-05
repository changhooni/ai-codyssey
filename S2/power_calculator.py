from flask import Flask

app = Flask(__name__)

def is_float_try(x):
    try:
        float(x)
        return True
    except ValueError:
        raise ValueError("Invalid number input.")
    
def is_int_try(x):
    try:
        int(x)
        return True
    except ValueError:
        raise ValueError("Invalid exponent input.")

def power_with_positive(base, exponent):
    kk = 1

    if exponent == 0:
        return "Zero division error"

    if exponent > 0:
        for _ in range(exponent):
            #print(f'squared_number1 : {result}')
            kk *= base
        if kk == 0:
            return "Zero division error"
        
        if is_float_try(kk):
            return kk
    else:
        for _ in range(abs(exponent)):
            kk /= base
            
        if kk == 0:
            return "Zero division error"
        #kk = 1.0 / kk
        if is_float_try(kk):
            return kk

def main():
    try:
        #print(f'{power_number}')
        #print(f'{input_number}')
        #def power(base, exponent):
        input_number = int(input('제곱을 구할 값을 입력하세요 : '))
        power_number = int(input('몇 제곱 값을 입력하세요 : '))

        if is_float_try(power_number):
            result = 0
            #print(input_number, '의', power_number, '제곱 = ', math.pow(input_number, power_number)) # math.pow() 함수를 사용하여 처리 방법
            #squared_number = power(input_number, power_number)
            #if is_int_try(input_number) == 0:
            #    raise ZeroDivisionError("Zero division error")
            
            #if power_number > 0:
            #    print('22')
            #    result = power_with_positive(input_number, power_number)  
            #    return print(f"Result1 : {result}")
            #else:  
            #    print('11')  
            result = power_with_positive(input_number, power_number)
            return print(f"Result : {result}")
        
            # for문에 _는 변수 값이 필요 없을 때 사용한다
            #if int(power_number) < 0:
            #    i = 0
            #    while i < power_number:
            #        result /= float(input_number)
            #        i += 1
                #tmp_list = [1, 2, 3, 4]
                #for n in tmp_list:
                #    result /= float(input_number)
                    #print(f'squared_number1 : {result}')
            #else:
            #    for _ in range(int(power_number)):
                    #print(f'squared_number1 : {result}')
            #        result *= float(input_number)
        else:            
            print("Invalid exponent input.")
        #result = eval(operator2)
        #print(f"Result : {result}")
    except ValueError as e:
        print(e)

    #except ZeroDivisionError:
    #    print("zero division error")

    #except Exception


#input_number = int(input('제곱을 구할 값을 입력하세요 : '))
#power_number = int(input('몇 제곱 값을 입력하세요 : '))
#s_number = s_number(input_number, power_number)
#squared_number = power(input_number, power_number)


if __name__ == "__main__":
    main()