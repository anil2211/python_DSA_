def min(a):
    min=float("inf")  #initialise miimum as positive infinity

    for num in a:
        if num<min:
            min=num
    return min

def max(a):
    max=float("-inf") # initilise maximum as negative infinity

    for num in a:
        if num>max:
            max=num
    return max           

if __name__ == "__main__":
    a=[4,8,5,6,1,2]
    n=len(a)
    print("minimum element is:",min(a))
    print("maximum element is:",max(a))