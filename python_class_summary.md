# Python 클래스 및 메소드 정리

## 클래스 기본 구조
```python
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

u = Unit("마린", 40, 5)
print(f"{u.name}: 체력 {u.hp}, 공격력 {u.damage}")
```

- `__init__`: 객체 생성 시 자동 호출되는 초기화 메서드
- `self`: 객체 자신을 의미, 모든 메서드의 첫 번째 매개변수로 필요
- 멤버 변수는 `self.변수명 = 값` 형식으로 초기화

## 기본 공격 유닛 클래스
```python
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력: {self.damage}]")

    def damaged(self, damage):
        self.hp -= damage
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")
```

- `attack`과 `damaged` 메서드를 통해 객체의 행동 정의
- `self.hp <= 0` 조건으로 파괴 여부 체크

## 레벨업 및 회복 응용
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
        print(f"{self.name} : 레벨 {self.level} 상승")

    def status(self):
        print(f"{self.name} : 체력 {self.hp}, 공격력 {self.damage}, 레벨 {self.level}")
```

- `level_up`에서 멤버 변수 증가
- `status` 메서드로 객체 상태 출력

## 아이템 상자 예제
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

- `self.list`를 누적해서 관리
- `gained`를 사용하면 획득 아이템 개수를 따로 출력 가능

## 스킬 시스템 응용
```python
class Character:
    def __init__(self, name, hp, mp, level=1, skills=None):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.level = level
        self.skills = skills if skills is not None else []

    def learn_skill(self, skill_name):
        self.skills.append(skill_name)
        print(f"{skill_name}을 익혔습니다. 스킬 리스트[{self.skills}]")

    def use_skill(self, skill_name):
        cost = 20
        if skill_name not in self.skills:
            print("습득하지 못한 스킬입니다.")
            return
        if self.mp < cost:
            print("마나가 부족합니다.")
            return
        self.mp -= cost
        print(f"{skill_name} 사용! [남은 마나: {self.mp}]")
```

- 스킬 리스트는 `append` 사용
- 마나 체크 및 스킬 습득 여부 확인 후 사용
- `skills=None` 및 조건부 초기화로 기본 리스트 공유 문제 방지

## 중요 포인트 정리
- `self`는 항상 첫 번째 매개변수로 사용
- `__init__`는 객체 생성 시 초기화, 다른 메서드는 일반 함수처럼 정의
- 리스트 누적 시 `append`, += 사용 시 문자열과 혼동 주의
- 조건문 부등호 (`<=`, `>=`)는 변수 값 기준으로 판단
- 파일입출력은 단순 읽기보다, 읽은 데이터를 리스트나 딕셔너리로 변형하여 활용하는 연습 필요

