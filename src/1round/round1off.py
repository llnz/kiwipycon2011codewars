'''
find most common pairing of letters
'''

if __name__ == '__main__':
    chromosome4 = list(open('1b.chr4.txt').read())
    
    prev = None
    curr = chromosome4[0]
    chromosome4 = chromosome4[1:]
    
    totals = {}
    
    while len(chromosome4) > 0:
        prev = curr
        curr = chromosome4[0]
        chromosome4 = chromosome4[1:]
        try:
            totals[prev+curr] += 1
        except:
            totals[prev+curr] = 1
    
    maxpair = None
    maxcount = 0
    for key, value in totals.items():
        if value > maxcount:
            maxpair = key
            maxcount = value
    
    print maxpair, maxcount
    