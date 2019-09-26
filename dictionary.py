import json
from difflib import get_close_matches,SequenceMatcher
def mkdict(word):
    data = json.load(open("data.json"))
    sugst = []
    sugst=get_close_matches(word,data.keys())
    if word in data:
        return (data[word])
    elif len(sugst) == 0:
        return("The word does not exsist. Please enter a valid word")
    else:
        if word.title() in data:
            return (data[word.title()])
        else:
            char = input("Looks like you have spelled something wrong, did you mean %s ?\nPlease input 'Y' for Yes and 'N' for No" %sugst[0])
            char.lower()
            if char == "y":
                word=sugst[0]
                return (data[word])
            else:
                return ("The word does not exsist. Please enter a valid word")
while True:
    word = str(input("Please enter a word:"))
    define = mkdict(word.lower())
    count=1
    if type(define) == list: 
        for i in define:
            print(count,".",i)
            count=count+1
    else:
        print(define)
    
            
        
