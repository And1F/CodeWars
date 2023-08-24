from copy import copy

def combos(number):
    ans = []
    output = [number]
    ans.append(copy(output))
    print(output)
    if number == 1:
        return [1]
    while output.count(1) != len(output):
        if output[-1] == 1:
            for i in range(1, number):
                if output[-i] != 1:
                    if i >= output[-i]:
                        rest = i
                        base = output[-i] - 1
                        output[-i] -= 1
                        del output[-i + 1:]
                        for q in range(number):
                            output.append(base)
                            rest -= base
                            if rest - base == 0:
                                output.append(base)
                                ans.append(sorted(output))
                                break
                            elif rest - base < 0:
                                output.append(rest)
                                ans.append(sorted(output))
                                break
                    else:
                        output[-i] -= 1
                        del output[-i + 1:]
                        output.append(i)
                        ans.append(sorted(output))
                        break
                    break
        elif output[-1] != 1:
            output[-1] -= 1
            output.append(1)
            ans.append(sorted(output))
    return ans
print(combos(5))