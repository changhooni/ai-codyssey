from flask import Flask

app = Flask(__name__)

num = list(map(float, input('숫자를 입력하세요 : ').split()))
#list 함수 등록된 값을 리스트 형식으로 반환한다
#map 함수는 여러 개의 데이터를 한 번에 다른 형태로 변환한다
min = num[0]
max = num[0]

for i in num:
    if i<min:
        min=i

    if i>max:
        max=i

def main():
    print(f"Result minimum : {min}, Result maximum : {max}")

if __name__ == '__main__':
    main()
