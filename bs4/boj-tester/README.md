# BOJ Tester

[Baekjoon Online Judge](https://www.acmicpc.net/) 문제의 샘플 입출력을 자동으로 테스트해줍니다.

- 2022.08.09. 제작

## Usage

```shell
$ python tester.py [Problem Number] [Your Python Filename]
```

```
Example:
python tester.py 1145 submit.py
python tester.py 01145 submit.py
python tester.py 1145 submit (.py 생략 가능)
```

## Dependency

```shell
pip install requests beautifulsoup4
```

## Example

1. 맞았을 때

![correct](https://user-images.githubusercontent.com/61629480/183429350-9ef6c3e2-aed8-41b7-a764-c42497e75132.png)

2. 틀렸을 때

![wrong](https://user-images.githubusercontent.com/61629480/183429358-c8d24f50-8c3d-467c-aa35-62c1d57a6027.png)

## 추가 예정 기능

- Python stderr의 경우 별도 표시
- Python 이외 언어로 확장
- 테스트를 통과하였을 경우, 제출과 제출 결과 보기 자동화
