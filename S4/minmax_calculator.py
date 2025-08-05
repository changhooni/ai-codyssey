from flask import Flask

app = Flask(__name__)

text_num = input('숫자를 입력하세요 : ')
#list 함수 등록된 값을 리스트 형식으로 반환한다

def find_max(i):
    max = i[0]

    for num in i:
        if num > max:
            max = num
    return max

def find_min(y):
    min = y[0]

    for num in y:
        if num < min:
            min = num
    return min
 

def main():
    try:
        numbers = [int(x) for x in text_num.split()]
        max_num = (float(find_max(numbers)))
        min_num = (float(find_min(numbers)))
        print(f"Result minimum : {min_num}, Result maximum : {max_num}")
    except ValueError:
        print("Invalid input.")

    #map 함수는 여러 개의 데이터를 한 번에 다른 형태로 변환한다
    

if __name__ == '__main__':
    main()
