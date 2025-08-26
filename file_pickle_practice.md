# 파일 입출력 & pickle 정리

## 1. 파일 입출력 기본

### 쓰기 (덮어쓰기)
```python
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()
```

### 이어쓰기
```python
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()
```

### 읽기
```python
# 전체 읽기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

# 한 줄씩 읽기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")
print(score_file.readline())
score_file.close()

# while 반복문 이용
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

# 리스트로 저장
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()
```

## 2. pickle 기본

### 저장
```python
import pickle
pro = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
pickle.dump(profile, pro)
pro.close()
```

### 불러오기
```python
pro = open("profile.pickle", "rb")
profile = pickle.load(pro)
print(profile)
pro.close()
```

## 3. 연습문제 예시

### 문제1 - 파일 저장/읽기
```python
# 입력받아 파일 저장
score_file = open("score.txt", "w", encoding="utf8")
subject = input("과목명 입력: ")
score = int(input("점수 입력: "))
print(f"{subject} : {score}", file=score_file)
score_file.close()

# 이어쓰기
score_file = open("score.txt", "a", encoding="utf8")
subject = input("과목명 입력: ")
score = int(input("점수 입력: "))
print(f"{subject} : {score}", file=score_file)
score_file.close()

# 읽기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()
```

### 문제2 - pickle 저장/불러오기
```python
import pickle
# 저장
pro = open("profile.pickle", "wb")
profile = {"이름":"김학생", "국어":80, "수학":65, "과학":76}
pickle.dump(profile ,pro)
pro.close()

# 불러오기
pro = open("profile.pickle", "rb")
load = pickle.load(pro)
print(load)
pro.close()
```

### 문제3 - pickle 점수 등급분류
```python
import pickle
# 저장
book = open("booknum", "wb")
bookpro = {"이름":"홍길동", "책점수": [85, 92, 78]}
pickle.dump(bookpro, book)
book.close()

# 불러와서 평균과 등급
book = open("booknum", "rb")
load = pickle.load(book)
book.close()

scores = load["책점수"]
total = sum(scores)
count = len(scores)
avg = total / count
if avg >= 90:
    grade = "Gold"
elif avg >= 70:
    grade = "Silver"
elif avg >= 50:
    grade = "Bronze"
else:
    grade = "Normal"

print(f"총점: {total}점, 평균: {avg:.2f}점 - 등급: {grade}")

# 파일로 저장
lod = open("lods.txt", "w", encoding="utf8")
print(f"총점: {total}점, 평균: {avg:.2f}점 - 등급: {grade}", file=lod)
lod.close()
```

## 4. 추가 연습 아이디어
- 여러 과목을 반복적으로 입력받아 파일에 이어쓰기
- pickle로 학생 여러 명 정보를 저장하고, 평균/등급 출력
- 파일과 pickle 데이터를 연동하여 읽기/쓰기
- 함수로 묶어서 재사용 가능하게 만들기

