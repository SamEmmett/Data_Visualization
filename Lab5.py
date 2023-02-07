import pandas as pd
import itertools as iter

def reader():
    with open('E:\Data_Mining\Lab 5\groceries.csv') as csvfile:
        wordstr = csvfile.read()
    
    wordstr = wordstr.replace('\n',',') # replaces the new line character with a comma
    wordlist = wordstr.split(',') #creates a list by spliting each word at the comma

    df = pd.DataFrame(wordlist)
    listed = df.value_counts()
    
    print(df.value_counts())

    ########### ------ OPTIONAL STUFF ------ ############
    listed = df.value_counts()[:6].index.tolist() #grabs the top 6 values and moves them to a list
    listed = list(iter.chain(*listed)) #this removes the tuple values and makes these just strings

    a = iter.combinations(listed, 1) # base list
    u = [' '.join(i) for i in a]

    b = iter.combinations(listed, 2) # 2 items each
    v = [' '.join(i) for i in b]

    c = iter.combinations(listed, 3) # 3 items each
    w = [' '.join(i) for i in c]

    d = iter.combinations(listed, 4) # 4 items each
    x = [' '.join(i) for i in d]

    e = iter.combinations(listed, 5) # 5 items each
    y = [' '.join(i) for i in e]

    f = iter.combinations(listed, 6) # 6 items each
    z = [' '.join(i) for i in f]

    print("BASE")
    print(u)
    print()
    print("COMBO 2")
    print(v)
    print()
    print("COMBO 3")
    print(w)
    print()
    print("COMBO 4")
    print(x)
    print()
    print("COMBO 5")
    print(y)
    print()
    print("COMBO 6")
    print(z)
    print()


if __name__ == '__main__':
    reader()