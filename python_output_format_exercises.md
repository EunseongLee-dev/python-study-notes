# Python 다양한 출력 포맷 & 응용 문제 정리

## 1. 다양한 출력 포맷 예제

```python
# 오른쪽 정렬, 총 10자리 확보
print("{0: >10}".format(500))

# 양수일 땐 +, 음수일 땐 - 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬, 빈칸을 _ 채움
print("{0:_<+10}".format(500))

# 3자리마다 콤마 찍기
print("{0:,}".format(100000000))

# 3자리마다 콤마, +- 부호 표시
print("{0:+,}".format(100000000))
print("{0:+,}".format(-100000000))

# 3자리마다 콤마, +-부호, 총 자리수 확보, 빈공간 ^ 표시
print("{0:^<+30,}".format(100000000000))

# 소숫점 출력
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))
```

## 2. f-string을 이용한 동일 출력

```python
# 오른쪽 정렬
print(f"{123: >10}")

# 왼쪽 정렬, _ 채움
print(f"{-456:_<10}")

# 3자리마다 콤마, 부호 표시
print(f"{987654321:+,}")

# 가운데 정렬, 부호, 콤마, 총 자리수 확보
print(f"{123456789:^+20,}")

# 소숫점 특정 자리까지 표시
print(f"{5/3:.2f}")
```

## 3. 조건문과 반복문 응용 예제

```python
# 난이도1: 대기번호 고객등급
for num in range(1, 16):
    if num % 3 == 0 and num % 5 == 0:
        vss = "VIP + 우수고객"
    elif num % 5 == 0:
        vss = "우수고객"
    elif num % 3 == 0:
        vss = "VIP"
    else:
        vss = "일반"
    print(f"대기번호: {num:03d}번 - {vss}")

# 난이도2: 1인당 금액 계산

def soo(total_amount, people):
    return total_amount / people

tot = int(input("사용하신 총 금액: "))
ple = int(input("인원 수 입력: "))
gs = soo(tot, ple)

print(f"총 금액: {tot:,}원, 인원: {ple}명\n1인당 내야 할 금액: {gs:,.2f}원")

# 난이도3: 함수로 고객등급 출력

def one(num):
    if num % 3 == 0 and num % 5 == 0:
        return "VIP + 우수고객"
    elif num % 5 == 0:
        return "우수고객"
    elif num % 3 == 0:
        return "VIP"
    else:
        return "일반"

def tow(last_num):
    for n in range(1, last_num+1):
        status = one(n)
        print(f"대기번호: {n:03d}번 - {status}")

last = int(input("방문 번호를 입력해주세요: "))
tow(last)

# 난이도4: 총점과 학생 수 입력 후 평균 등급 출력

def one(score, student):
    return score / student

def tow(total_score, student_count):
    avg = one(total_score, student_count)
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    else:
        grade = "D"
    print(f"평균 점수: {avg:.2f}점 - 등급: {grade}")

total_score = int(input("총 점수 입력: "))
student_count = int(input("학생 수 입력: "))
tow(total_score, student_count)
```

