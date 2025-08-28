# 학생별 독서 기록 관리 - 학습 힌트/정리

## 오늘 학습 핵심 및 헷갈렸던 부분

### 1. 학생명과 도서 기록을 딕셔너리로 여러 번 저장
- 처음 시도: `pickle.dump(la, std)` + `pickle.dump(aa, std)` → 안 됨
- 문제점: 매번 dump하면 학생명과 도서 기록이 별도로 저장되며, pickle.load 시 한 번에 하나만 불러와짐
- 해결: **한 학생의 정보 전체를 하나의 딕셔너리로 묶어서 저장**
  ```python
  student = {"학생명": la, "books": book}
  pickle.dump(student, std)
  ```
- 힌트: 입력 루프는 도서명과 대출일수만, 학생명은 루프 밖에서 한 번만 입력

### 2. pickle에서 불러온 데이터 구조 처리
- 구조: `student = {"학생명": '홍길동', "books": {도서명: 일수, ...}}`
- 헷갈렸던 점: 딕셔너리 안에 딕셔너리(`books`)가 있어서 단순 for문 돌리면 원하는 대출일수와 도서명을 따로 빼오기 어려움
- 해결 힌트:
  - 도서 목록과 대출일수 함께 출력하려면 `.items()` 사용
  - 값만 리스트로 뽑아 평균 계산하려면 `.values()` 사용
  ```python
  book_values = list(ac["books"].values())
  book_items = list(ac["books"].items())
  ```

### 3. 출력 포맷 문제
- 초기 시도: for문 안에서 바로 print → 반복될 때마다 학생명 출력, 결과가 혼란스러움
- 해결: 도서 기록을 리스트에 저장 후 `join`으로 묶어서 한 번만 출력
  ```python
  ab = []
  for a, b in book_items:
      ab.append(f"{a}({b}일)")
  ass = ", ".join(ab)
  print(f"학생명: {name}\n대출 기록: {ass}\n총 대출일수: {tot}일\n평균 대출일수: {mix:.2f}일\n등급: {op}")
  ```

### 4. 평균 계산 및 등급 판정
- 총 대출일수: `tot = sum(book_values)`
- 평균: `mix = tot / len(book_values)`
- 등급 조건:
  ```python
  if mix >= 30:
      op = "Bookworm"
  elif mix >= 20:
      op = "Active Reader"
  elif mix >= 10:
      op = "Casual Reader"
  else:
      op = "Rarely reads"
  ```

### 5. 학습 힌트
- 여러 데이터를 pickle에 저장할 때는 **한 번에 한 구조로 묶어서 dump** 해야 편리
- for문과 join 활용하면 출력 포맷 깔끔하게 정리 가능
- 딕셔너리 안에 딕셔너리 구조는 `.items()`와 `.values()` 조합으로 쉽게 접근 가능
- 반복적으로 헷갈리거나 막히면 구조를 먼저 시각적으로 그려보고, 어떤 자료형에 접근해야 하는지 확인하는 습관이 도움됨

