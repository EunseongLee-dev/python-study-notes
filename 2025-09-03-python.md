# 상속, 오버라이딩, super() 정리

## 1. 상속 기본

- 클래스 정의 시 상위 클래스 지정: `class 하위클래스(상위클래스):`
- 하위 클래스는 상위 클래스의 속성과 메서드를 **자동으로 상속**.
- 상위 클래스의 속성 초기화는
  - `상위클래스.__init__(self, ...)`
  - 또는 `super().__init__(...)` 사용 가능

```python
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.max_hp = hp

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        self.damage = damage
```

## 2. 하위 클래스 메서드에서 상위 클래스 속성 사용

- 하위 클래스 메서드에서 상위 클래스 속성을 사용하려면, 상위 클래스에서 정의된 `self.name`, `self.hp` 등을 그대로 접근 가능
- 외부 객체 참조 시 `target.name`, `target.hp`처럼 사용

```python
marin = AttackUnit("마린", 50, 10)
file = AttackUnit("파이어뱃", 60, 20)

marin.attack(file)  # file.hp 접근 가능
```

## 3. 오버라이딩(Overriding)

- 하위 클래스에서 **부모 클래스 메서드와 동일한 이름**으로 새 메서드를 정의하면 기존 메서드를 덮어쓰게 됨
- 부모 메서드를 유지하면서 확장하려면 `super().메서드()` 사용

```python
class Vehicle:
    def move(self):
        print("Vehicle 이동")

class Car(Vehicle):
    def move(self):
        print("Car 이동")
        super().move()  # 부모 메서드도 호출
```

- 부모 기능만 호출하거나, 완전히 자식 기능으로 대체하고 싶으면 `super()` 호출 없이 새 메서드만 정의하면 됨

## 4. 연습 포인트

- 상속으로 부모 속성/메서드를 활용하는 법
- 외부 객체(target) 참조 시 `객체.속성` 사용
- 오버라이딩 후 부모 메서드 유지 여부 판단
- `super()` 활용 시 부모 초기화 및 메서드 호출 가능

