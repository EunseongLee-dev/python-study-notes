# 오늘 학습 내용 정리 (모듈, 패키지, 전투 시스템)

## 1. 모듈(Module)

- 다른 파일에 정의된 코드(함수, 클래스)를 재사용 가능하게 하는 파일 단위
- 불러오기 방법
```python
import module_name
module_name.func()

import module_name as mn
mn.func()

from module_name import func
func()

from module_name import func as f
f()
```
- `as` 키워드로 별칭 사용 가능
- `from module_name import *` : 모든 함수/클래스를 가져옴 (단, __all__에 정의된 것만 가져오는 경우 있음)

### 모듈 직접 실행 확인
```python
if __name__ == "__main__":
    # 직접 실행 시 실행되는 코드
```
- `__name__` : 현재 모듈 이름
- `__main__` : 직접 실행 시 모듈 이름

### 모듈 위치 확인
```python
import inspect
print(inspect.getfile(module_name))
```
- 현업에서는 파일 경로를 확인하거나, 프로젝트 구조 파악 용도로 사용

---

## 2. 패키지(Package)

- 모듈을 묶어 놓은 디렉토리
- 구조 예시:
```
travel/
  __init__.py
  thal.py
  viet.py
```

- 사용 방법
```python
import travel.thal
trip = travel.thal.Thail()
trip.detail()

from travel.thal import Thail
trip = Thail()
trip.detail()

from travel import viet
trip = viet.vietnam()
trip.detail()
```
- `__all__` : `from package import *` 시 가져올 모듈 목록 제한

---

## 3. 전투 시스템 구현 시 실수 및 팁

1. Player와 Monster 클래스 안에서 attack, take_damage를 각각 만들 필요 없음
   - 외부에서 Battle 클래스 안에서 처리하면서 다른 객체(target)를 인자로 전달

2. attack, take_damage 메서드 분리 여부
   - 요구사항에 따라 분리했지만, 로직 상 묶어도 무방
   - 기능적으로 묶을 수 있는 경우 묶는 습관 가지기

3. 체력 반영 문제
   - `target.hp - self.atk` 만 쓰면 변수 값 갱신 안됨 → `target.hp -= self.atk` 필요

4. 예외 처리
   - 클래스 내부에서 try-except 사용 vs 외부에서 처리
   - 외부에서 처리하면 오류 메시지 출력 후 프로그램 자연스럽게 진행 가능

5. attack 메서드 동작 이해
   - 외부에서 생성한 객체(몬스터, 플레이어)를 target으로 전달하면 메서드 내부에서 체력, 상태 모두 반영됨
   - 예시:
```python
play1.attack(mons1)  # play1의 공격력이 mons1에 반영
mons1.attack(play1)  # mons1의 공격력이 play1에 반영
```

---

## 4. 오늘 문제풀이 중 햇갈린 부분

- -=, +=, *=, //= 등 연산자 사용 시 변수 값 갱신 여부 확인
- 예외처리 발생 시 try 내부 코드 중단, 외부 try에서 잡으면 이후 코드 실행 가능
- 모듈, 패키지 import 방식 여러 가지 (import, from, as) 숙지 필요
- Battle 클래스 설계 시 Player, Monster 클래스를 상속할 필요 없음, 객체 전달 방식 사용
- attack, take_damage를 외부에서 객체 간 연동 시 체력 반영 확인

