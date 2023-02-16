lst = [3,5,99999,15,48,2,69,420]

for i in range(len(lst)-1):
    for j in range((len(lst)-1)-i):
        if lst[j]>lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)