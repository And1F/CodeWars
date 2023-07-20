def runoff(voters):
    candidates = voters[0]
    while True:
        ranking = [0 for _ in range(len(voters[0]))]
        for voter in voters:
            ranking[candidates.index(voter[0])] += 1
        print(ranking, candidates)
        if max(ranking) > len(voters)/2: 
            return candidates[ranking.index(max(ranking))]
        elif len(set(ranking)) == 1:
            return None    
        else:
            for num in range(len(voters)):
                voters[num] = [x for x in voters[num] if x not in [candidates[index] for index, num in enumerate(ranking) if num == min(ranking)]]
            candidates = [x for x in candidates if x not in [candidates[index] for index, num in enumerate(ranking) if num == min(ranking)]]


print(runoff([     ['Daisuke Aramaki', 'Brian J. Mason', 'Gihren Zabi', 'Frank Underwood'], 
              ['Brian J. Mason', 'Frank Underwood', 'Gihren Zabi', 'Daisuke Aramaki'], 
              ['Gihren Zabi', 'Frank Underwood', 'Daisuke Aramaki', 'Brian J. Mason'], 
              ['Gihren Zabi', 'Daisuke Aramaki', 'Frank Underwood', 'Brian J. Mason'], 
              ['Daisuke Aramaki', 'Gihren Zabi', 'Brian J. Mason', 'Frank Underwood'], 
              ['Gihren Zabi', 'Daisuke Aramaki', 'Frank Underwood', 'Brian J. Mason'], 
              ['Brian J. Mason', 'Frank Underwood', 'Gihren Zabi', 'Daisuke Aramaki']]))

