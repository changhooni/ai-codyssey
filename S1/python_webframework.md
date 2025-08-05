python에 대표 웹프레임워크는 3가지가 존재한다 
1. django
2. flask
3. FastAPI

django의 특정
1) Django (풀스택 프레임워크)
공식 문서에서 "마감기한이 있는 완벽주의자를 위한 웹 프레임워크(The web framework for perfectionists with deadlines)" 로 소개하고 있다. 완전한 사용성을 위해 필요한 모든 기능을 갖췄다는 의미로 batteries-included library 로도 불리는 Django는 MVT(Model - View - Template) 아키텍처로 구성되어 있다.
- django에 구조는 Model Layer, View Layer, Template Layer 로 구성되어 있다
Model Layer 는 데이터 구조 저장
View Layer 는 유저 요청 처리 및 변환
Template Layer 는 사용자에게 표시할 화면 구조(html, 프론드엔드) 처리

- Model Layer를 통해 내장 ORM(Object-Relational Mapping: 객체 모델과 관계형 dbms 테이블 간 맵핑 기법)을 제공하면서, 자동으로 관리자 인터페이스 등을 제공하여 이러한 기능들을 직접 구현할 필요 없이 이용할 수 있다는 장점이 있다.

단점: 무겁고 유연성이 떨어질 수 있음.

2) flask (마이크로 프레임뭐크)
Django는 웹 개발을 위해 필요할 것으로 예상되는 틀을 기본적으로 제공하는 반면,
Flask는 마이크로 웹 프레임워크의 형식으로 최소한의 기능만 기본적으로 제공하며 직접 유연하게 필요한 기능만 플러그인 형식으로 추가하게 된다.
공식문서에 따르면 아래 3가지 기술에 의존성을 띄고 있으며, 각각 다음과 같은 기능을 처리하고 있다.

Werkzeug WSGI(Web Server Gateway Interface) toolkit는 웹 서버 및 HTTP 요청 처리
Jinja template engine는 html 등 마크업 언어에 동적 컨텐츠를 삽입할 수 있는 기능 제공
Click CLI toolkit는 command line interface 구현

단점: Django에 비해 기능이 적고, 개발 속도가 느릴 수 있음.

3) FastAPI (고성능 API 프레임워크)
이름에서와 같이 속도 측면에서 우위를 보이는 웹 프레임워크
ASGI(Asynchronous Server Gateway Interface)를 통해 비동기를 가능하게 해줌으로써 기존 WSGI를 사용하던 프레임워크보다 빠른 성능을 보여주고 있다.
사용법은 Flask와 같이 간편하게 decorator로 라우팅 설정을 해주며, async를 통해 비동기 설정을 해줄 수 있다.

단점: Django나 Flask에 비해 커뮤니티 규모가 작음.