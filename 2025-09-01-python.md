## Python 클래스 기초 정리

### 1. 클래스 정의와 객체 생성
```python
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

# 객체 생성
marine = Unit("마린", 40, 5)
print(f"{marine.name}: 체력 {marine.hp}, 공격력 {marine.damage}")
```
- `Unit` 클래스 정의
- `__init__` 생성자: 객체 생성 시 초기화
- `self.name`, `self.hp`, `self.damage`: 멤버변수

---

### 2. 멤버변수와 기본값 매개변수
```python
class Unit:
    def __init__(self, name, hp, damage, clocking=False):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.clocking = clocking

# 객체 생성
w1 = Unit("레이스", 80, 5, clocking=True)
w2 = Unit("레이스", 80, 5)

print(f"{w1.name}: 체력 {w1.hp}, 공격력 {w1.damage}, 클로킹 {w1.clocking}")
print(f"{w2.name}: 체력 {w2.hp}, 공격력 {w2.damage}, 클로킹 {w2.clocking}")
```
- `clocking=False`로 기본값 설정 가능
- 객체별로 멤버변수 값 독립적

---

### 3. 오늘 응용 복습 포인트
- 여러 객체를 리스트에 담아 반복문으로 관리
- 멤버변수 접근하여 상태 출력
- 기본값 매개변수 활용

```python
units = [
    Unit("마린", 40, 5),
    Unit("메딕", 60, 0),
    Unit("파이어뱃", 50, 8),
    Unit("레이스", 80, 5, clocking=True),
    Unit("탱크", 150, 35)
]

for u in units:
    print(f"{u.name}: 체력 {u.hp}, 공격력 {u.damage}, 클로킹 {u.clocking}")
```
- 반복문으로 객체 상태 확인
- 객체별 속성 출력
- `clocking` 속성은 기본값 또는 True 선택 가능

---
### 핵심 정리
1. 클래스는 객체를 만들기 위한 틀
2. `__init__`는 생성자, 객체 초기값 설정
3. `self.변수`로 멤버변수 생성, 객체마다 독립적
4. 기본값 매개변수로 선택적 속성 가능
5. 여러 객체를 리스트에 담아 반복문으로 관리 가능

