# using brute force

def repeat(x):
    _size=len(x)
    repeated=[]
    for i in range(_size):
        k=i+1
        for j in range(k,_size):
            if x[i]==x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

list1=[10,20,30,20,20,30,40,50,-20,60,-20,-20]
print(repeat(list1))

# using single loop
list2=[10,20,30,20,20,30,40,50,-20,60,-20,-20]
unique_list=[]
duplicate=[]

for i in list2:
    if i not in unique_list:
        
        unique_list.append(i)
    elif i not in duplicate:
        print(i)
        duplicate.append(i)

print(duplicate)
print(unique_list)