# Python 다중상속 정리

## 오늘 배운 내용 포인트

1. **다중상속 기본 구조**
   - 클래스 선언 시 괄호 안에 여러 부모 클래스를 나열
     ```python
     class ChildClass(Parent1, Parent2):
         pass
     ```
   - 겹치지 않는 부모 클래스끼리 상속할 때는 문제 없음

2. **super()와 다중상속**
   - 단일상속에서는 `super().__init__()`가 간편하고 권장
   - 다중상속에서 super() 사용 시 MRO(Method Resolution Order) 때문에 주의 필요
   - 겹치는 부모 클래스가 있을 경우 직접 부모 클래스 호출 방식이 더 직관적일 수 있음

3. **다중상속과 조부모 클래스**
   - 부모 클래스가 다른 클래스를 상속하고 있을 경우, 자식 클래스는 조부모 클래스도 상속받음
   - 예: `SpaceAttackUnit(AttackUnit, Flyable, ShieldMixin)` → AttackUnit이 Unit을 상속하므로 SpaceAttackUnit에서도 Unit 메서드 사용 가능

4. **메서드 오버라이딩 활용**
   - 자식 클래스에서 부모 메서드를 재정의 가능
   - 조건에 따라 move()에서 fly() 또는 attack()를 호출하고, attack()는 오버라이딩된 print()가 추가로 실행되도록 설계

5. **Mixin 클래스 사용**
   - ShieldMixin처럼 기능별로 독립적인 클래스 정의 후 다중상속으로 확장 가능
   - take_damage()는 shield가 남아있으면 shield에서 먼저 차감하고, 남는 데미지는 hp에서 차감

## 문제풀면서 메모해두면 좋은 부분

- 다중상속 시 부모 클래스의 속성(`self.name`, `self.hp`, `self.shield`) 접근 방법
- move()와 attack() 오버라이딩 동작 순서와 조건문 설계
- ShieldMixin에서 shield가 음수로 내려갈 경우 hp 차감 계산 방법 (`self.hp += self.shield`) 이해
- super()와 직접 부모 클래스 호출 차이점 및 MRO 영향
- 다중상속에서 부모-조부모 관계 이해, show_status()와 같은 조부모 메서드 활용

---

**Tip:** 오늘처럼 다중상속 + 오버라이딩 + Mixin을 함께 사용하는 구조는 프로젝트에서 흔하게 등장하므로, 각 메서드의 동작 순서와 상속 관계를 그림이나 표로 시각화해두면 이해가 훨씬 빠름.

