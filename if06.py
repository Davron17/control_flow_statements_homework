def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    k=0
    if a<0:
        k+=1
    if b<0:
        k+=1
    if c<0:
        k+=1
    if k>3-k:
        print("there are a lot of negative numbers")
    if k<3-1:
        print("there are a lot of positive numbers")
    return k
print(main(-2,4,1))
print(main(3,-3,-6))