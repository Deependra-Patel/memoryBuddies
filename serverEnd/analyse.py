f = open("temp.txt", "rb")
f1 = open("temp2.txt", "rb")
f2 = open("out1", "w")
f3 = open("out2", "w")
count = 0
count1 = 0
a1 = []
a2 = []
try:
    byte = f.read(1)
    while len(byte) != 0:
        num = 0
        for i in range(4):
            if len(byte) != 0:
                num = num*256 + ord(byte)
                byte = f.read(1)
        # f2.write(str(num)+"\n")
        a1.append(num)
    a1.sort()
    print(a1[1])

    print("here")

    byte = f1.read(1)
    while len(byte) != 0:
        num = 0
        for i in range(4):
            if len(byte) != 0:
                num = num*256 + ord(byte)
                byte = f1.read(1)
        # f3.write(str(num)+"\n")
        a2.append(num)
    a2.sort()
    print(a2[1])

    ind1 = 0
    ind2 = 0
    len1 = len(a1)
    len2 = len(a2)
    count = 0

    print(len1)
    print(len2)
    val = 0

    curr = 0
    cunt = 0

    for i in range(len1-1):
        if (a1[i] == a1[i+1]):
            curr = curr + 1
        else:
            if (curr > cunt):
                cunt = curr
                val = a1[i]
            curr = 0

    if (curr > cunt):
        cunt = curr
        val = a1[len-1]

    print(cunt)
    print(val)

    cunt = 0
    a3 = []
    
    while((ind1 < len1) and (ind2<len2)):
        if (a1[ind1] == a2[ind2]):
            count = count + 1
            ind1 = ind1 + 1
            ind2 = ind2 + 1
            a3.append(a1[ind1])
        elif (a1[ind1] < a2[ind2]):
            ind1 = ind1 + 1
        else:
            ind2 = ind2 + 1

    print(count)
    print(cunt)
    print(len(set(a3)))
            
    
finally:
    f.close()
    f1.close()
    f2.close()
    f3.close()
