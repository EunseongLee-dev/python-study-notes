# 오늘 배운 주요 내용 정리 (깃허브 업로드용)

## 1. 상속과 super()
- 하위 클래스에서 상위 클래스의 속성과 메서드를 물려받을 수 있음.
- 상위 클래스의 `__init__`를 호출할 때 `super().__init__(...)`를 사용하면 간단하게 상위 속성을 초기화 가능.
- 예시:
```python
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        self.damage = damage
```
- `super()`를 사용하면 명시적으로 부모 클래스 이름을 쓰지 않아도 됨.

## 2. 오버라이딩(Overriding)
- 하위 클래스에서 상위 클래스의 메서드를 동일한 이름으로 재정의.
- 필요하면 `super().메서드()`를 통해 부모 메서드 기능도 함께 호출 가능.
- 예시:
```python
class Lion(Animal):
    def make_sound(self):
        super().make_sound()  # 부모 클래스 소리 출력
        print("어흥!")       # 추가 동작
```

## 3. 기본 속성 초기화와 리스트
- 매개변수 없이도 `self.team = []`처럼 클래스 안에서 속성을 초기화 가능.
- 리스트를 초기화하면 하위 메서드에서 `.append()`로 요소를 추가 가능.
- 주의: `team=None` 같은 매개변수를 쓸 때는 기본값을 적절히 처리해야 함.

## 4. __repr__과 __str__
- `__str__`: 사용자 친화적인 출력용.
- `__repr__`: 개발자용, 객체 상태를 정확히 표현.
- 리스트나 파일 입출력 시 `__repr__` 정의하면 객체를 문자열로 변환 가능.
- 예시:
```python
def __repr__(self):
    return f"{self.name} {self.age}세({self.grade}학년)"
```

## 5. 파일 입출력(with + txt)
- 기본 구조:
```python
with open("filename.txt", "w", encoding="utf8") as f:
    for obj in obj_list:
        f.write(str(obj) + "\n")

with open("filename.txt", "r", encoding="utf8") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
```
- `with` 사용으로 파일 닫는 과정 자동 처리.
- `readlines()`는 줄 단위로 읽음, 각 줄 끝에는 `\n`이 포함되어 있으므로 `strip()`으로 제거.
- 리스트에 있는 객체들을 파일에 쓰고 싶을 때는 `__repr__` 또는 `str()` 사용.

## 6. today point
- `self.oo = []` 같은 초기화, `super()`, 오버라이딩, `__repr__`, 파일 입출력(with, readlines, strip) 등 이전에 헷갈렸던 포인트를 재정리.
- 요구사항이 모호한 문제에서는 일단 필수 기능 위주로 구현 후, 확장 기능은 나중에 적용 가능.
- 깃허브 업로드는 새로운 개념/기능 위주로 기록하고, 단순 복습은 로컬 정리로 충분.

