
def insertion_sort(a):
    for i in range(1,len(a)):
        key = a[i]
        j= i-1
        # print("la key es " + str(key) + " y jota es " + str(a[j]))
        # print("estoy parado en " + str(key)+ " y tengo atras a " + str(j))
        while j >= 0 and a[j] > key:
            # print("estoy parado en " + str(key)+ " y tengo atras a " + str(j))
            a[j+1]=a[j]
            j -= 1
        a[j+1] = key

    print(a)
    return a



insertion_sort([5,2,4,6,1,3,7,8,9])
