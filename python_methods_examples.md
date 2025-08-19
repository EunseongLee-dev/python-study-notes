# Python 메서드 정리 및 예시 (조건문/반복문 중심)

## 1. 문자열 관련

| 메서드 | 설명 | 예시 | 사용 예시 코드 |
|--------|------|------|----------------|
| `.lower()` | 문자열을 모두 소문자로 변환 | `"Hello".lower()` → `"hello"` | `if c.lower() in "aeiou": ...` |
| `.upper()` | 문자열을 모두 대문자로 변환 | `"Hello".upper()` → `"HELLO"` | `if c.upper() == "A": ...` |
| `.isalpha()` | 알파벳 문자 여부 확인, True/False 반환 | `"abc".isalpha()` → `True`, `"abc1".isalpha()` → `False` | `if i.isalpha(): ...` |
| `.isdigit()` | 숫자로만 구성되어 있는지 확인, True/False 반환 | `"123".isdigit()` → `True`, `"12a".isdigit()` → `False` | `if ch.isdigit(): ...` |
| `.strip()` | 문자열 양쪽 공백 제거 | `"  hello  ".strip()` → `"hello"` | `word = input().strip()` |
| `.replace(old, new)` | 문자열 내 old를 new로 변경 | `"abc".replace("a","x")` → `"xbc"` | `text = text.replace(" ", "")` |
| `.split(sep)` | 문자열을 구분자 sep 기준으로 분리하여 리스트 반환 | `"a,b,c".split(",")` → `["a","b","c"]` | `lst = input().split()` |
| `.join(iterable)` | 리스트 등의 요소를 문자열로 연결 | `"".join(["a","b","c"])` → `"abc"` | `result = "".join(lst)` |

---

## 2. 리스트 관련

| 메서드 | 설명 | 예시 | 사용 예시 코드 |
|--------|------|------|----------------|
| `.append(x)` | 리스트 마지막에 x 추가 | `lst.append(5)` | `numbers.append(i)` |
| `.insert(i, x)` | 리스트 i번째 위치에 x 삽입 | `lst.insert(1, 99)` | `lst.insert(0, val)` |
| `.pop(i)` | 리스트 i번째 요소 제거 및 반환 | `lst.pop(0)` | `val = lst.pop()` |
| `.remove(x)` | 리스트에서 값 x 제거 | `lst.remove(5)` | `lst.remove(val)` |
| `.sort()` | 리스트 오름차순 정렬 | `lst.sort()` | `lst.sort()` |
| `.reverse()` | 리스트 요소 순서 뒤집기 | `lst.reverse()` | `lst.reverse()` |
| `len()` | 리스트 길이 반환 | `len(lst)` | `length = len(lst)` |

---

## 3. 범용 함수

| 함수 | 설명 | 예시 | 사용 예시 코드 |
|------|------|------|----------------|
| `range(start, end, step)` | 지정 범위의 숫자 생성 | `range(1, 10, 2)` → 1,3,5,7,9 | `for i in range(1, num+1): ...` |
| `input()` | 사용자 입력 받기 (문자열) | `name = input("이름: ")` | `user = input()` |
| `int()`, `str()` | 자료형 변환 | `int("123")` → 123, `str(123)` → "123" | `num = int(input())` |
| `sum(iterable)` | 합계 계산 | `sum([1,2,3])` → 6 | `total = sum(lst)` |
| `min(iterable)`, `max(iterable)` | 최소/최대 값 반환 | `min([1,2,3])` → 1 | `max_val = lst[0]; for i in lst: if i>max_val: max_val=i` |

---

## 4. 난수 관련

| 함수 | 설명 | 예시 | 사용 예시 코드 |
|------|------|------|----------------|
| `randint(a, b)` | a 이상 b 이하 정수 난수 반환 | `randint(1, 100)` | `target = randint(1,100)` |
| `choice(seq)` | 리스트 등에서 랜덤 요소 선택 | `choice([1,2,3])` | `pick = choice(lst)` |

---

# Python 자주 쓰는 메서드 정리 (조건문/반복문 활용 기준)

## 1. 문자열 관련 메서드

### 1.1 isalpha()
- 설명: 문자열이 알파벳으로만 이루어져 있는지 확인
- 반환: True / False
- 사용 예시:
```python
s = 'abc'
print(s.isalpha())  # True
s2 = 'abc123'
print(s2.isalpha()) # False
```

### 1.2 isdigit()
- 설명: 문자열이 숫자로만 이루어져 있는지 확인
- 반환: True / False
- 사용 예시:
```python
s = '123'
print(s.isdigit())  # True
s2 = '12a3'
print(s2.isdigit()) # False
```

### 1.3 lower()
- 설명: 문자열을 모두 소문자로 변환
- 사용 예시:
```python
s = 'Hello'
print(s.lower())  # hello
```

### 1.4 upper()
- 설명: 문자열을 모두 대문자로 변환
- 사용 예시:
```python
s = 'Hello'
print(s.upper())  # HELLO
```

### 1.5 in
- 설명: 문자열 안에 특정 문자가 있는지 확인
- 반환: True / False
- 사용 예시:
```python
s = 'apple'
print('a' in s)  # True
print('b' in s)  # False
```

## 2. 리스트 관련 메서드

### 2.1 append()
- 설명: 리스트 끝에 값 추가
- 사용 예시:
```python
lst = [1, 2]
lst.append(3)
print(lst)  # [1, 2, 3]
```
- 주의: 괄호 안에 추가할 값을 넣어야 함. 빈 괄호는 오류 발생.

### 2.2 sort()
- 설명: 리스트를 오름차순으로 정렬
- 사용 예시:
```python
lst = [3, 1, 2]
lst.sort()
print(lst)  # [1, 2, 3]
```
- 내림차순: `lst.sort(reverse=True)`

### 2.3 reverse()
- 설명: 리스트 순서를 역순으로 변경
- 사용 예시:
```python
lst = [1, 2, 3]
lst.reverse()
print(lst)  # [3, 2, 1]
```

### 2.4 len()
- 설명: 리스트 또는 문자열 길이 반환
- 사용 예시:
```python
lst = [1, 2, 3]
print(len(lst))  # 3
s = 'abc'
print(len(s))    # 3
```
