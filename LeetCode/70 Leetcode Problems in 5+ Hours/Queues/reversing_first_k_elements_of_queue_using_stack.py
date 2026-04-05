def reverseFirstK(q : list, k : int) -> list:
    sub = q[0:k]
    q[0:k] = sub[::-1]
    return q

print(reverseFirstK(q=[10,20,30,40,50,60,70,80,90,100], k=5))