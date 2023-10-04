def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a%2==0 and a>99:
        print("three-digit odd number")
    if a%2==1 and a>99:
        print("three-digit even number")
    if a%2==0 and 99>a>9:
        print("two-digit odd number")
    if a%2==1 and 99>a>9:
        print("two-digit even number")
    return a
print(main(153))
print(main(25))
print(main(22))
print(main(152))