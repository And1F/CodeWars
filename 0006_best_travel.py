import itertools
def choose_best_sum(limit, count_of_numbers, lst1):
    lst = lst1
    lst = sorted(lst)
    ans = -10000000
    combinations = itertools.combinations(lst, count_of_numbers)
    for combination in combinations:
        current_sum = sum(combination)
        if limit - current_sum == 0:
            return current_sum
        elif 0 < limit-current_sum < limit - ans:
            ans = current_sum
    if ans == -10000000:
        return None
    return ans

print(choose_best_sum(331, 2, [91, 74, 73, 85, 73, 81, 87]))