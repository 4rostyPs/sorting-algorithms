sampleList = [3,2,7,1,5,4]

for i in range(1,len(sampleList)):
    key = sampleList[i]
    j = i - 1
    while key < sampleList[j] and j>=0:
        sampleList[j+1]=sampleList[j]
        j -= 1
    sampleList[j+1] = key
print(sampleList)
