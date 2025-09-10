# Python 예외처리 요약

## 1. 기본 try/except
- try: 실행 코드 블록
- except [에러명] as [변수]: 에러 처리 블록
- 예제:
```python
try:
    num = int(input("숫자를 입력하세요: "))
except ValueError as e:
    print("숫자만 입력해주세요.")
```
- `as e`는 임의의 이름. 에러 객체를 변수로 받아 사용할 수 있음.

## 2. 여러 에러 처리
- 여러 except 블록을 사용해 각각 다른 에러 처리 가능
```python
try:
    result = num1 / num2
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("숫자만 입력해주세요.")
except Exception as err:
    print("알 수 없는 에러 발생", err)
```
- `Exception`은 모든 예외를 포괄하는 상위 클래스.

## 3. 의도적 에러 발생 (raise)
- 조건 충족 시 직접 예외 발생 가능
```python
if num1 >= 10 or num2 >= 10:
    raise ValueError("한 자리 숫자만 입력하세요")
```
- except 블록에서 처리 가능

## 4. 사용자 정의 예외
```python
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
```
- raise BigNumberError("메시지") 로 호출 가능
- except BigNumberError as err: 로 처리 가능

## 5. finally
- 오류 발생 여부와 상관없이 항상 실행되는 블록
```python
finally:
    print("계산기를 이용해 주셔서 감사합니다.")
```
- 마무리 처리, 리소스 정리 등에 사용

## 6. 연습 시 유의점
- 입력값은 기본적으로 문자열로 들어오므로 숫자로 처리할 때는 `int()` 변환 필요
- 여러 입력값을 받을 때는 `split()` 후 반복문을 통해 int 변환
- 연산자는 문자열로 입력받아 조건문으로 처리
- 반복문 안에서도 try/except 사용 가능, 상황에 따라 범위 조절

## 7. 예외처리 흐름 요약
1. try 블록 실행
2. 에러 발생 시 해당 except 블록 실행
3. finally 블록 실행 (있으면)
4. 프로그램 계속 진행

## 8. 실습 핵심 포인트
- 숫자 입력 체크
- 음수/범위 체크 (사용자 정의 예외 활용)
- 연산자 조건 처리
- 리스트 여러 값 처리
- 결과 출력 전 변수에 누적 계산
- finally로 마무리 출력

