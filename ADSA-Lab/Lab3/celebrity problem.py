def celebrity_problem_n(M, n):
    row = [0] * n
    col = [0] * n
    celebrity = M[0][0]
    for i in range(n):
        if M[celebrity][i] == 1:
            celebrity = i
    for i in range(n):
        if i != celebrity:
            if M[celebrity][i] == 1 or M[i][celebrity] == 0:
                return -1

    return celebrity

def celebrity_problem_n_square(M, n):
    for i in range(n):
        knows_no_one = True
        known_by_everyone = True

        for j in range(n):
            if M[i][j] == 1:
                knows_no_one = False
            if M[j][i] == 0 and i != j:
                known_by_everyone = False

        if knows_no_one and known_by_everyone:
            return i

    return -1

ans = celebrity_problem_n([[0, 0, 1, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 0],
                         [0, 0, 1, 0]], 4)
if ans == -1 :
    print("No Celebrity")
else :
    print("Celebrity is:", ans)

ans = celebrity_problem_n_square([[0, 0, 1, 0],
                                 [0, 0, 1, 0],
                                 [0, 0, 0, 0],
                                 [0, 0, 1, 0]], 4)
if ans == -1 :
    print("No Celebrity")
else :
    print("Celebrity is:", ans)