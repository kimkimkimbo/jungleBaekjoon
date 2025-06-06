#해시 테이블



"""
서로 다른 두 키가 같은 인덱스를 가지게 되면 충돌이 일어남

충돌 해결법 2가지

1. 채이닝
같은 인덱스에 여러 값을 연결 리스트로 저장하는 방식

Hash Table:
[0] → 없음  
[1] → 없음  
[2] → ("apple", 10) → ("grape", 22)  
[3] → 없음  
같은 해시 값이 나오면 리스트에 쭉쭉 붙임
구현이 쉽고, 메모리를 더 사용함

2. 개방 주소법
빈 자리를 찾아서 그 다음 칸, 그다음 칸을 순회하면서 저장

table 크기: 5

hash("a") = 2  
hash("b") = 2 ← 충돌 발생!

개방 주소법은 이런 식:
2 → 사용 중이니  
3 → 비었으면 여기에 b를 저장

방식 종류
선형 탐사 (Linear probing): 한 칸씩 순차적으로
이차 탐사 (Quadratic probing): 1², 2², 3²...씩 점프
이중 해싱 (Double hashing): 다른 해시 함수로 점프 크기 결정

파이썬 dict: 체이닝 아님, 개방 주소법 변형 사용
자바 HashMap: 체이닝 방식 (Java 8부터는 트리로 최적화도 함)
C++ unordered_map: 체이닝
"""