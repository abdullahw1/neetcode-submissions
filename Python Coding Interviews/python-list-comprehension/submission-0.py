from typing import List


def create_list_of_odds(n: int) -> List[int]:
    arr=range(1, n + 1)
    res = [i for i in arr if i%2 != 0]
    return res


# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))
