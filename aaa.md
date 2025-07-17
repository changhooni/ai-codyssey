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


git 설정 확인 명령어
git config --list

git 개행문자 설정
git config --global core.autocrlf input -> mac os
git config --global core.autocrlf true -> window os

git 사용자 이름 이메일 변경
git config --global user.name "사용자 이름"
git config --global user-email "사용자 이메일"

git 기본 브랜치명 변경
git config --global init.defaultBranch 명칭

git core.editor 확인 방법
git config --global core.editor 명령어 실행

git core.editor 설정 명령어
git config --global core.editor "code --wait"


Git 명령어 목록입니다. 
저장소 관련 명령어:
git init: 현재 디렉토리에 새로운 Git 저장소를 초기화합니다.
git clone [저장소 주소]: 원격 저장소를 복제하여 로컬에 저장합니다.
git remote add [저장소 이름] [저장소 주소]: 원격 저장소를 추가합니다.
git remote -v: 원격 저장소 목록을 확인합니다.
git remote remove [저장소 이름]: 원격 저장소를 삭제합니다.
git fetch: 원격 저장소의 변경 사항을 가져오지만 병합하지는 않습니다.
git pull: 원격 저장소의 변경 사항을 가져와 로컬 저장소와 병합합니다.
git push: 로컬 저장소의 변경 사항을 원격 저장소로 업로드합니다. 
작업 트리 관련 명령어:
git status: 작업 트리의 변경 상태를 확인합니다.
git add [파일 이름]: 변경 사항을 스테이징 영역에 추가합니다.
git add .: 변경된 모든 파일을 스테이징 영역에 추가합니다.
git commit -m "[커밋 메시지]": 스테이징 영역의 변경 사항을 커밋합니다.
git commit -am "[커밋 메시지]": 변경 사항을 커밋하고 스테이징 영역에 추가합니다.
git reset [파일 이름]: 스테이징 영역에서 파일을 제거합니다.
git rm [파일 이름]: 파일 및 스테이징 영역에서 삭제합니다.
git mv [기존 파일 이름] [새로운 파일 이름]: 파일 이름을 변경합니다.
git log: 커밋 기록을 확인합니다.
git log --oneline: 커밋 기록을 한 줄로 요약하여 확인합니다.
git log -p: 커밋 기록과 함께 변경 사항을 확인합니다.
git diff: 작업 트리와 마지막 커밋 사이의 변경 사항을 확인합니다.
git diff --staged: 스테이징 영역과 마지막 커밋 사이의 변경 사항을 확인합니다. 
브랜치 관련 명령어:
git branch: 브랜치 목록을 확인합니다.
git branch [브랜치 이름]: 새로운 브랜치를 생성합니다.
git checkout [브랜치 이름]: 다른 브랜치로 전환합니다.
git merge [브랜치 이름]: 다른 브랜치의 변경 사항을 현재 브랜치로 병합합니다.
git branch -d [브랜치 이름]: 브랜치를 삭제합니다.
git branch -D [브랜치 이름]: 강제로 브랜치를 삭제합니다. 
기타 명령어:
git config --list: Git 설정을 확인합니다.
git config --global user.name "[이름]": 전역 사용자 이름을 설정합니다.
git config --global user.email "[이메일]": 전역 사용자 이메일을 설정합니다.
git help [명령어]: 특정 명령어에 대한 도움말을 확인합니다.
git stash: 변경 사항을 임시로 저장합니다.
git stash list: 임시로 저장된 변경 사항 목록을 확인합니다.
git stash pop: 임시로 저장된 변경 사항을 복원합니다.
git tag: 태그 목록을 확인합니다.
git tag [태그 이름]: 현재 커밋에 태그를 추가합니다.
git checkout [태그 이름]: 특정 태그가 가리키는 커밋으로 이동합니다. 