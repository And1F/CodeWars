def find_missing(sequence):
    distance = [sequence[x]-sequence[x-1] for x in range(1,len(sequence))]
    distance = distance[0] if distance[0] == distance[1] else distance[-1]
    for i in range(len(sequence)):
        if sequence[i] + distance != sequence[i+1]: return sequence[i]+distance


print(find_missing([-2, -9, -16, -30, -37, -44, -51, -58, -65]))