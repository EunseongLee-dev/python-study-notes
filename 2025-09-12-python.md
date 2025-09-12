# 오늘 학습 복습 정리

## 1. pip
- Python 패키지 관리 도구
- 주요 명령어
  - `pip list` : 설치된 패키지 확인
  - `pip show <패키지명>` : 패키지 정보 확인
  - `pip install <패키지명>` : 패키지 설치
  - `pip uninstall <패키지명>` : 패키지 삭제
- 예시 : `pip install beautifulsoup4`

## 2. 내장 함수 (Built-in functions)
- Python에서 기본 제공되는 함수들
- 주요 함수 예시
  - `print()`, `len()`, `type()`, `dir()`, `abs()`, `round()` 등
- 특징 : import 없이 바로 사용 가능

### 활용 예시
```python
print(dir())  # 현재 네임스페이스 확인
import random
print(dir(random))  # random 모듈 함수 확인
```

## 3. 외장 모듈 (External modules)
- import 해서 사용해야 하는 모듈들
- 예시
  - `os` : 운영체제 기능 제공
    - `os.getcwd()`, `os.listdir()`, `os.makedirs()`, `os.rmdir()`
  - `glob` : 폴더/파일 경로 조회
    - `glob.glob('*.py')`
  - `time` : 시간 관련 함수
    - `time.localtime()`, `time.strftime()`
  - `datetime` : 날짜/시간
    - `datetime.date.today()`, `datetime.timedelta(days=100)`

## 4. 복습 포인트
1. `dir()`를 이용해 객체가 가진 함수/속성을 확인 가능
2. 내장 함수와 외장 모듈의 차이를 명확히 이해
3. 필요 시 구글링과 공식 문서 활용

## 5. 추가 메모
- `max(value, 0)` : hp가 음수로 내려가지 않게 제한할 때 활용
- 반복문과 조건문 조합으로 공격/체력/사망 판정 처리 가능
- `getattr(obj, '속성명')`, `setattr(obj, '속성명', 값)` : 동적 속성 접근 및 수정
- 스킬 사용 가능 여부 처리 패턴
  - True/False 플래그로 스킬 사용 가능 여부 관리
  - 반복문 안에서 조건 확인 후 공격 및 사용 처리
- 이번 한 달 동안의 학습 범위에서는 **기본적인 함수/모듈 이해와 클래스 설계 감각**이 가장 중요

