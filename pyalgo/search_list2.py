# 순차 탐색
# 리스트의 첫번째 자료부터 하나씩 비교하면서 같은 값이 나오면
# 그 위치를 돌려주고(반환), 못찾으면 -1을 반환함

def search_list(a, x):
    n = len(a)
    for i in range(0, n):
        if a[i] == x:
            return name[i]
    return '?'


v = [60, 5, 33, 12, 97]
name = ['이순신', '강감찬', '서희', '안중근', '유관순']


# 매개변수 - 리스트, 찾는값
print(search_list(v, 5))  # 1
print(search_list(v, 12))  # 3
print(search_list(v,100))  # 3




