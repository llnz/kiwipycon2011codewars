'''
How many words from the dictionay can be made form 
the letter in "codewars"? Can use each letter only once,
don't have to use all letters

'''

if __name__ == '__main__':
    wordlist = open('1a.dictionary.txt').readlines()
    
    codewars = 'codewars'
    
    count = 0
    
    cwset = set(list(codewars))
    
    for word in wordlist:
        wordset = set(list(word.strip()))
        #print wordset
        if wordset.issubset(cwset):
            dupset = set()
            dupfound = False
            for letter in word:
                if letter in dupset:
                    dupfound = True
                    break
                dupset.add(letter)
            
            #print word
            if not dupfound:
                count += 1
    
    print count
    
#also for dup letter check
#if len(word.strip()) != len(wordset)

