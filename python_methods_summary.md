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

## 3. 랜덤 관련 메서드

### 3.1 randint(a, b)
- 설명: a~b 사이의 랜덤 정수 반환
- 사용 예시:
```python
from random import randint
num = randint(1, 10)  # 1~10 사이 랜덤값
```

---

> 이 문서는 조건문/반복문 활용 기준으로 자주 쓰이는 메서드만 정리한 확장판입니다.
> 문제 풀이 시 바로 참고할 수 있도록 구성했습니다.

