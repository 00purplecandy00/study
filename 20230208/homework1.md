```
실습 목록
MySQL 개발 환경 구축
가이드를 보고, MySQL 개발 환경을 구축합니다.

가이드는 세 단계로 구성 되어있습니다.

MySQL 설치
Workbench 설치 및 MySQL 접속
실습용 데이터베이스 준비
MySQL 개발 환경 구축 가이드

자신만의 Workbench 활용 가이드 작성
제공 받은 가이드가 아닌 자신만의 Workbench 활용 가이드를 작성합니다.

가이드는 마크다운(.md) 포맷을 활용해서 작성합니다.

가이드에는 두 가지 내용을 필수적으로 포함합니다.

Workbench 활용 MySQL 접속 방법
실습 데이터베이스에 대한 쿼리(Query)문 작성 및 쿼리문 실행 방법
```



```
제 맥북이 구형이라서 (카탈리나 OS) 적어주신 방법으로는 설치가 안되서 구글링을 통해 모든 설치를 완료했습니다
```

## 1. MySQL 설치
```
구글에 mysql 검색 > mysql > community
https://downloads.mysql.com/archives/community/

에서 카탈리나(mac x)에 맞는 버전 선택 후 설치
설치완료 후 환경설정 맨 아래에 있는 mysql 버튼 활성화 확인
```
## 2. Workbench 설치 및 MySQL 접속
```
노션에 있는 링크에서 저에게 맞는 버전을 확인해서 설치한 뒤
비밀번호 설정하는 것은
아래 블로그를 참고했습니다
https://velog.io/@sorzzzzy/MySQL-Mac-MySQL-root-%EB%B9%84%EB%B0%80%EB%B2%88%ED%98%B8-%EC%B4%88%EA%B8%B0%ED%99%94%ED%95%98%EA%B8%B0
```
## 3. 실습용 데이터베이스 준비
```
노션에서 다운받았습니다
https://hyper-growth.notion.site/MySQL-6af14bcbda94447f8dbe29a308985dc5#46cdb47a1f744daca69977965ea06c65
```
## 4. MySQL 개발 환경 구축 가이드
```
Workbench 활용 MySQL 접속 방법
```
```
환경설정 아래에 있는 mysql 아이콘 클릭 후 mssql 실행 중인지 확인 후
launchpad에 들어가서 mysql workbench 아이콘 더블클릭해서 실행합니다
비밀번호 자동입력 설정을 해놓아서 그대로 실행됩니다
```
======================================================================================
```
실습 데이터베이스에 대한 쿼리(Query)문 작성 및 쿼리문 실행 방법
```
```
workbench 실행 후 Mysql connections > Local instance 3306 클릭
쿼리문 작성 후
실행버튼(번개모양 버튼) 클릭

```