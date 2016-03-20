import sys
def table(list):
    for candidate in list:
        print("%8s %8s")%(candidate[0],candidate[1])

f = sys.argv[1]


with open(f) as fp:
    total = []
    for line in fp:
        votes = line.split(', ')
        votes = [x.strip('\n') for x in votes]
        votes = [x.lower() for x in votes]
        for x in votes:
            total.append(x)
    tally = [[x,total.count(x)] for x in set(total)]
    tally.sort(key=lambda x: int(x[1]), reverse=True)
    table(tally)




