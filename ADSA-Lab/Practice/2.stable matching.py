def stable_matching(men_preferences, women_preferences):
    n = len(men_preferences)
    free_men = list(range(n))
    engaged = [None] * n  # woman -> man
    men_next_proposal = [0] * n  # next woman to propose

    women_rank = [
        {man: rank for rank, man in enumerate(prefs)}
        for prefs in women_preferences
    ]

    while free_men:
        man = free_men.pop(0)
        woman = men_preferences[man][men_next_proposal[man]]
        men_next_proposal[man] += 1

        if engaged[woman] is None:
            engaged[woman] = man
        else:
            current_man = engaged[woman]
            if women_rank[woman][man] < women_rank[woman][current_man]:
                engaged[woman] = man
                free_men.append(current_man)
            else:
                free_men.append(man)

    matches = [(engaged[w], w) for w in range(n)]
    return matches

# Example usage:
men_prefs = [
    [0, 1, 2],
    [2, 0, 1],
    [1, 2, 0]
]
women_prefs = [
    [2, 1, 0],
    [0, 1, 2],
    [1, 2, 0]
]

result = stable_matching(men_prefs, women_prefs)
print("Stable matches (man, woman):", result)