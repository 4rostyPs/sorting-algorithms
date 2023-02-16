sampleList = [1,3,5,7,9,0,2,4,6,8,10]

for i in range(len(sampleList)):
    smallest = i 
    for j in range(i+1,len(sampleList)):
        if sampleList[j] < sampleList[smallest]:
            smallest = j
    sampleList[i], sampleList[smallest] = sampleList[smallest], sampleList[i]
    print(sampleList)

print(sampleList) 