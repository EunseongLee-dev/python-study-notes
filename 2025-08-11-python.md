# 리스트(List)와 사전(Dictionary) 정리

## 📌 리스트(List)

### 1. 리스트 생성
```python
fruits = ["사과", "바나나", "오렌지"]
empty_list = []
```

### 2. 주요 메서드
| 메서드 | 설명 | 예시 |
|--------|------|------|
| append(x) | 리스트 끝에 요소 추가 | `fruits.append("포도")` |
| insert(i, x) | 지정한 위치 i에 요소 추가 | `fruits.insert(1, "망고")` |
| pop([i]) | i 위치 요소 제거 후 반환 (기본값: 마지막) | `removed = fruits.pop()` |
| sort() | 오름차순 정렬 (원본 변경) | `nums.sort()` |
| reverse() | 순서 뒤집기 (원본 변경) | `nums.reverse()` |
| clear() | 모든 요소 삭제 | `fruits.clear()` |
| extend(iterable) | 다른 리스트 요소를 현재 리스트에 추가 | `a.extend(b)` |

### 3. 주의점 ⚠️
- `append()`는 **하나의 값**만 추가 가능. 여러 개 추가 시 `extend()` 사용.
- `extend()`는 리스트를 **직접 변경**하며 반환값이 `None`.
- `sort()`는 **원본 변경**, 반환값 `None`. 정렬된 새 리스트 필요 시 `sorted()` 사용.
- `pop()`은 삭제한 요소를 반환 → 변수에 저장 가능.

---

## 📌 사전(Dictionary)

### 1. 사전 생성
```python
person = {"name": "Tom", "age": 25, "city": "Seoul"}
empty_dict = {}
```

### 2. 주요 메서드 & 연산
| 메서드/연산 | 설명 | 예시 |
|-------------|------|------|
| dict[key] | 키로 값 조회 (없으면 오류) | `person["name"]` |
| get(key, default) | 키 값 조회 (없으면 default 반환) | `person.get("age", 0)` |
| in | 키 존재 여부 확인 | `"name" in person` |
| del dict[key] | 특정 키-값 삭제 | `del person["city"]` |
| keys() | 모든 키 반환 (dict_keys 객체) | `person.keys()` |
| values() | 모든 값 반환 | `person.values()` |
| items() | (키, 값) 쌍 반환 | `person.items()` |

### 3. 주의점 ⚠️
- 존재하지 않는 키 접근 시 `dict[key]`는 오류 발생 → `get()` 권장.
- `keys()`, `values()`, `items()`는 **반복문에서 주로 사용**.
- `in`은 **키 기준**으로만 확인 (값은 아님).

---

## 💡 요약
- 리스트: 순서 O, 중복 O, 인덱스로 접근 가능.
- 사전: 순서 X(파이썬 3.7+에서는 입력 순서 유지), 키 중복 불가, 값은 중복 가능.
