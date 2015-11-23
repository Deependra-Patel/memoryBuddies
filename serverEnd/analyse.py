#!/usr/bin/python3

f1 = open("../memTraces/Trace1/VM1.txt5", "rb")
f2 = open("../memTraces/Trace1/VM1.txt6", "rb")
a1 = []
a2 = []

a1 = f1.readlines()
a2 = f2.readlines()
a1.sort()
a2.sort()
ind1 = 0
ind2 = 0
len1 = len(a1)
len2 = len(a2)
count = 0
print("No. of pages in file 1: " + str(len1))
print("No. of pages in file 2: " + str(len2))

while((ind1 < len1) and (ind2<len2)):
    if (a1[ind1] == a2[ind2]):
        count = count + 1
        ind1 = ind1 + 1
        ind2 = ind2 + 1
        continue;
    elif (a1[ind1] < a2[ind2]):
        ind1 = ind1 + 1
    else:
        ind2 = ind2 + 1

print("Common hashes: "+str(count))