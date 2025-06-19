

# without using zip function create a dictionary from two list ?

list1=[11,22,33,44,55,66]
list2=['aim','banana','cat','dog','eag']
dict={}
for i in range(len(list1)):
    dict[list1[i]]=list2[i]
    print(dict)

# create adictionary of frq of a each character in a strings ?
a="python is a proramming language"
b={}
for ch in a:
    if ch in b:
        b[ch]+=1
    else:
        b[ch]=3
        print(b)

