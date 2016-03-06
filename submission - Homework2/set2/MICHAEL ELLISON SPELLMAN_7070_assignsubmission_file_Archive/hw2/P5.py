def problem5(x, roots):
    answer = 1
    for r in roots:
        answer *= (x - r)
    return answer


print problem5(2.3,[-1,1,2])
