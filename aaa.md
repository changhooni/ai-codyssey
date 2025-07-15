맥os 환경에서 python flask를 설치를 오류처리 방법
테이널에서 설치 명령어 
pip install flask

설치 진행 시 아래와 같은 문구 나오면 처리 방법
경구 문구 
WARNING: The script flask is installed in '/var/data/python/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

경고 내용은 해당하는 경로에 대한 path 설정이 되어 있지 않아 생기는 문제 
해결법
터이널에서 아래 명령어 입력
export PATH=$PATH:경로
ex) export PATH=$PATH:/var/data/python/bin

이렇게 처리 완료


파이썬 가상서버 만들기
vscode 터미널에서 아래 명령어를 입력하여 가상디렉토리(또는 폴더)를 생성합니다. 
python -m venv venv(다른 명칭으로 선정 가능)

디렉터리(풀더) 생성이 되어 있는지 확인 한다 

다시 vscode 터미널에서 가상서버를 실행하는 명령어를 아래에 같이 입력한다
맥os, 리눅스 = source venv/bin/activate
윈도우os = .\venv\Scripts\activate (또는 .\venv\Scripts\activate.bat)

터미널 앞에 ((venv)) 라는 마크가 생설될걸 알수 있다

가상서버 종류는 아래 명령어를 입력하면 된다
deactivate

