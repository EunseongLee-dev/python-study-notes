## Python 클래스 & 메소드 정리

### 1. 기본 클래스 작성
```python
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

u = Unit("마린", 40, 5)
print(f"{u.name}: 체력 {u.hp}, 공격력 {u.damage}")
```

### 2. 멤버변수 기본값, 선택적 매개변수
```python
class Unit:
    def __init__(self, name, hp, damage, clocking=False):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.clocking = clocking

w1 = Unit("레이스", 80, 5, clocking=True)
w2 = Unit("레이스", 80, 5)
```

### 3. 클래스 리스트 활용 & 파일 입출력
```python
ss = []
with open("units.txt", "r", encoding="utf8") as f:
    for line in f:
        parts = line.strip().split(",")
        ss.append(parts)

Unt = []
for i in ss:
    name, hp, damage = i[0], int(i[1]), int(i[2])
    clocking = True if i[3] == "True" else False
    obj = Unit(name, hp, damage, clocking)
    Unt.append(obj)
```

### 4. 공격 유닛 & 메소드
```python
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 공격 중입니다. [공격력: {self.damage}]")

    def damaged(self, damage):
        self.hp -= damage
        print(f"{self.name} : {damage} 공격을 받았습니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

    def heal(self, amount):
        self.hp += amount
        print(f"{self.name} : 체력이 {amount} 회복되었습니다.")
        print(f"{self.name} : 현재 남은 체력은 {self.hp} 입니다.")
```

### 5. 캐릭터 레벨업 예제
```python
class Character:
    def __init__(self, name, hp, damage, level=1):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.level = level

    def level_up(self):
        self.level += 1
        self.hp += 10
        self.damage += 2

    def status(self):
        print(f"{self.name} : 체력 {self.hp}, 공격력 {self.damage}, 레벨 {self.level}")
```

### 6. 아이템 상자 누적 예제
```python
from random import randint

class ItemBox:
    def __init__(self, name, list_item=0):
        self.name = name
        self.list = list_item

    def open_box(self):
        gained = randint(1, 5)
        self.list += gained
        print(f"아이템 {gained}개 획득")

    def show_items(self):
        print(f"현재 상자에 아이템 총 갯수는 {self.list}개 입니다.")
```

### 7. 스킬 학습/사용 예제
```python
class Character:
    def __init__(self, name, hp, mp, level=1, skills=None):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.level = level
        self.skills = [] if skills is None else skills

    def learn_skill(self, skill_name):
        self.skills.append(skill_name)

    def use_skill(self, skill_name):
        cost = 20
        if skill_name not in self.skills:
            print("습득하지 못한 스킬입니다.")
            return
        elif self.mp < cost:
            print("마나가 부족합니다.")
            return
        self.mp -= cost
        print(f"{skill_name} 사용! [남은 마나: {self.mp}]")
```

### 8. 포인트 정리
- `__init__`는 클래스 인스턴스 생성시 필수적으로 초기화하는 함수, 매개변수 self는 항상 첫번째
- 멤버변수 기본값 지정 가능: 선택 매개변수는 `=값` 형태
- 리스트 멤버변수 초기화 시 `None` 체크 후 `[]`로 초기화 추천
- `append()` 사용해 리스트에 아이템/스킬 누적
- 마나/체력 계산 시 self 변수 직접 수정, 누적 계산 주의
- 부등호 사용시 의미 정확히 이해: `<=`는 “~이하”, `>=`는 “이상”
