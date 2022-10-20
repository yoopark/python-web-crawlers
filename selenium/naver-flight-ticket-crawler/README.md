# 네이버 항공권 검색 자동화

이 프로그램은 다음의 일을 수행합니다.

1. 네이버 항공편 검색 결과 URL을 검색한다.
2. HTML을 파싱하여 **내가 원하는 시간대, 가격 조건에 맞는 항공편이 나왔는지** 찾는다.
3. 조건에 맞는게 없다면 30초의 텀을 두고 다시 1로 돌아간다.
4. 조건에 맞는게 나왔다면 환경변수로 저장되어 있던 **메일로 내게쓰기한다**.
5. (내가 보낸 메일에 알림이 오도록 설정해놓았다면 휴대폰으로 알림을 받아볼 수 있다)

- 2022.10.20. 제작

## Usage

```
# .env
NAVER_ID={네이버 아이디}
NAVER_PW={네이버 비밀번호}
```

```shell
python crawler.py
```

## Dependency

- selenium : Mac의 경우, `brew install chromedriver`로 쉬운 설치 가능
- `pip install python-dotenv`

## 비고

- 실행 전에 넣어두어야 하는 네이버 항공편 검색결과 URL도 사실 쪼개서 날짜, 승객 등을 인자로 받을 수도 있지만, 자동화로 검색해야 할 정도면 이미 날짜, 승객은 확정된 경우가 많을 것으로 예상되어 굳이 장황하게 만들지 않았음.
- 원래는 카카오톡 내게 보내기 기능을 활용하려 하였으나 카카오 API를 사용하려면 사전 동의 작업이 복잡하고, 무엇보다 내게 보내도 알림이 뜨진 않는다고 하여 포기하였음.