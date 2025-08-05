def add(a, b):
    return a + b
 
def subtract(a, b):
    return a - b
 
def multiply(a, b):
    return a * b
 
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a / b


def priority_retrun(exp):
    # numbers = 0
    tks = exp.split()
    n = len(tks)
    i = 0
    while i < n:
        if tks[i] in ('*', '/'):
            left = float(tks[i - 1])
            right = float(tks[i + 1])

            if tks[i] == '*':
                result = multiply(left, right)
            elif tks[i] == '/':
                result = divide(left, right)
            # 연산 결과로 치환
            tks[i - 1:i + 2] = [str(result)]
            
            i = max(i - 1, 0)
        else:
            i += 1

    result = float(tks[0])

    i = 1
    while i < len(tks):
        op = tks[i]
        num = float(tks[i + 1])
        if op == '+':
            result = add(result, num)
        elif op == '-':
            result = subtract(result, num)

        i += 2

    return result
    # kk = 0
    # ff = data[1]
    # result = 0
    # while i < n:
    #     kk = data[i]
    #     if i % 2 == 1:
    #         target = ['*', '/']
    #         if any(substring in kk for substring in target):
    #             if kk == '*':
    #                 a = int(data[i-1])
    #                 b = int(data[i+1])
    #                 result = multiply(a, b)
    #                 numbers = result
    #                 print(f'1=={numbers}')
    #             elif kk == '/':
    #                 if int(numbers) > 0:
    #                     a = int(numbers)
    #                     b = int(data[i+1])
    #                     if b == 0:
    #                         result = 'zero'
    #                     else:
    #                         result = divide(a, b)
    #                 else:
    #                     a = int(data[i-1])
    #                     b = int(data[i+1])
    #                     result = divide(a, b)
    #                 numbers = result
    #             print(f'2=={numbers}')
    #         else:                
    #             if int(numbers) > 0:
    #                 a = numbers
    #                 b = int(data[i-1])

    #                 if kk == '+':
    #                     result = add(a, b)
    #                 elif kk == '-':
    #                     result = subtract(a, b)
    #             else:
    #                 if int(numbers) > 0:
    #                     a = numbers
    #                     b = int(data[i+1])

    #                     if kk == '+':
    #                         result = add(a, b)
    #                     elif kk == '-':
    #                         result = subtract(a, b)
    #                 else:
    #                     a = int(data[i-1])
    #                     b = int(data[i+1])

    #                     if kk == '+':
    #                         result = add(a, b)
    #                     elif kk == '-':
    #                         result = subtract(a, b)

    #         numbers = result
    #         print(f'3=={numbers}')

    #     i += 1
    # return numbers
    
    #for i in range(n):
    #    for j in range(i+1, n):
    #        exponent.append(j)
    #return exponent



def main():
    cal_txt = input('계산 연산식을 등록하세요(Ex: 2 + 3 - 1 * 5 / 1) : ')
    #try: 
    priority_result = priority_retrun(cal_txt)
    print(f'{priority_result}')
    #except ValueError:
    #    print('Invalid input.')


if __name__ == '__main__':
    main()