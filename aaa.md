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
