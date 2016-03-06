list1=[3,5,2.3,5,10,4.2]

def maxminave(list1):
    minimum=min(float(s) for s in list1)
    maximum=max(float(s) for s in list1)
    avg=sum(list1)/len(list1)
    return minimum, maximum, avg

print(maxminave(list1))