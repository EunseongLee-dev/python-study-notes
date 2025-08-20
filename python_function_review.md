# Python 함수 복습 정리

## 1. 기본 함수 구조
```python
# 함수 정의
def 함수명(매개변수):
    수행할 코드
    return 반환값 # 필요시 사용

# 함수 호출
함수명(인자)
```
- `print()`는 함수 안에서 출력할 때 사용, return은 함수 밖에서 결과를 활용할 때 사용.
- 함수 호출 시 인자(값)를 넣어주면 매개변수와 연결되어 처리됨.

## 2. 매개변수와 반환값
```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result) # 8
```
- 매개변수는 함수 안에서 활용할 값.
- return은 함수 밖으로 값을 보내는 역할.
- print는 함수 안에서 바로 출력 가능, return은 변수에 담아 외부에서 활용 가능.

## 3. 기본값 매개변수
```python
def cafe(menu="아메리카노", size="Tall"):
    print(f"{size} 사이즈 {menu} 주문 완료!")

cafe()                  # Tall 사이즈 아메리카노 주문 완료!
cafe(size="Grande")     # Grande 사이즈 아메리카노 주문 완료!
cafe(menu="라떼")       # Tall 사이즈 라떼 주문 완료!
```
- 기본값이 있으면 호출 시 생략 가능.
- 순서대로 연결되며, 이름 지정 호출 가능.

## 4. 조건문/반복문과 함수
```python
def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'

print(grade(85)) # B
```
- 함수 안에서 조건문을 활용 가능.
- return으로 값을 반환하면 함수 밖에서 받아서 출력 가능.

## 5. 가변 인자 (*args)
```python
def mysum(*args):
    total = 0
    for num in args:
        total += num
    return total

print(mysum(10, 20, 30)) # 60
```
- *args는 몇 개의 인자가 들어올지 모를 때 사용.
- args는 튜플 형태로 받아서 반복문 등으로 처리 가능.
- 변수명은 관례상 args 사용, 다른 이름도 가능(*numbers, *values 등).

## 6. 문자열 합치기 예제
```python
def concat(*words):
    result = ''
    for w in words:
        result += w
    return result

print(concat("안녕", "하세요", "!!")) # 안녕하세요!!
```
- 여러 개의 문자열을 *args로 받아서 하나로 합칠 수 있음.

## 7. 중요 포인트
- 함수 안에서 print와 return의 차이를 확실히 이해.
- 기본값 매개변수와 이름 지정 호출 활용.
- *args를 사용하면 인자 개수 제한 없이 함수 설계 가능.
- 조건문/반복문과 함께 사용 시 흐름 이해 필수.
- 변수명은 관례일 뿐, *args처럼 *붙은 가변인자는 함수 정의 시 관례적으로 사용.
- 메서드(.lower(), .isalpha(), .append() 등)는 함수 안/외부 어디서든 상황에 맞게 활용 가능.
