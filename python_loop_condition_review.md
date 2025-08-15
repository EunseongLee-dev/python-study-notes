# Python - 반복문 및 조건문 학습 포인트 정리

## 1. for와 while 사용 기준

### for문

- **정해진 범위나 리스트/튜플의 요소를 순회할 때 사용**
- 예시

```python
for i in range(1, 11):  # 1~10까지
    print(i)
```

- 포인트
  - 반복 횟수가 명확한 경우.
  - 순회 대상이 리스트/범위 등 **정해져 있을 때**.

### while문

- **조건을 만족하는 동안 반복하고 싶을 때 사용**
- 예시

```python
i = 10
while i > 0:
    print(i)
    i -= 1
```

- 포인트
  - 반복 횟수가 미정이거나 사용자 입력/동적 조건에 따라 달라지는 경우.
  - `while True:`를 쓰고 내부에서 `break`로 종료하는 방식도 있음.

### 비교 요약

| 구분    | 사용 조건           | 예시             |
| ----- | --------------- | -------------- |
| for   | 반복 범위가 명확       | range, 리스트, 튜플 |
| while | 반복 범위 불명, 조건 기반 | True, 변수 비교    |

## 2. 조건문 if/elif/else 사용 포인트

- `if` : 독립적인 조건 체크
- `elif` : 앞 조건이 False일 때만 체크, 연속 조건
- `else`: 앞 조건들이 모두 False일 때 실행

```python
x = 10
if x > 5:
    print('5보다 큼')
elif x % 2 == 0:
    print('짝수임')
else:
    print('기타')
```

- 포인트
  - 독립 조건이면 다시 `if` 써도 됨
  - 연속 조건이면 `elif`로 연결
  - 마지막 catch-all은 `else`

## 3. break와 continue 사용

- **break** : 반복문 전체 종료
- **continue** : 이번 반복만 건너뛰고 다음 반복으로

```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)  # 1~4 출력

for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)  # 짝수만 출력
```

- 포인트
  - 조건 순서 중요
  - 루프 변수 갱신 시 위치(continue/break 전후)에 따라 결과 달라짐

## 4. input()과 f-string 포인트

- `input(prompt)` : 사용자 입력 받기 + prompt 출력
- `f-string` : 문자열 안에서 변수/연산 표현 가능

```python
cnt = 0
num = int(input('숫자를 입력해주세요: '))
print(f'입력값: {num}, 남은횟수: {3 - cnt}')
```

- 포인트
  - `3 - cnt`처럼 연산 가능
  - while 루프 안에서 cnt 변화에 따라 실시간 출력 가능

## 5. 오늘 학습 중 햇갈렸던 포인트 정리

- for vs while 시작 시 변수 생성 여부
- if, elif, else 연결 방식과 독립 조건 구분
- break/continue 사용 시 위치와 우선순위
- f-string 내부에서 연산 처리
- input() 출력 원리 (prompt)
- 누적 변수 갱신과 출력 순서

## 6. 개선 및 평가

- 지금까지 학습 상태

  - 큰 틀(for/while 구조, break/continue 용도)은 이해 시작
  - 세부 문법(조건문 연결, 루프 내 변수 갱신, 입력 처리)은 여전히 참조 필요
  - 이전 대비 개선: 문제를 풀면서 **햇갈리는 포인트를 스스로 인식**하고 있음
  - 원점 느낌이 있는 이유: 반복문과 조건문을 **즉각적으로 적용하는 능력**은 아직 불안정

- 향후 전략

  - 오늘처럼 **조건문 + 루프 + 변수 누적** 문제 위주로 집중 연습
  - 문제 풀면서 **조건 우선순위와 break/continue 위치** 머릿속으로 그림 그리기
  - for/while 기본 패턴 암기보다 **상황별 사용 감각**을 점차 강화

