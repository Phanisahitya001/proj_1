import operator
w=input("Please enter a string: ")
def most_frequent(string):
    d=dict()
    for key in string:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    x=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
    for i in x:
        print(i,"=",str(0)+str(x[i]))
a=(most_frequent(w))
