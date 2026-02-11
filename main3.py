def factorail(x):
    """this is a recursive function to find the factorail of an integer"""

    if x==0 or x==1:
        return 1
    else:
        return x*factorail(x-1)
    print("the factorial of 0",factorail(0))
    print("the factorial of 1",factorail(1))
    print("the factorial of 2",factorail(2))
    print("the factorial of 5",factorail(5))
    print("the factorial of 10",factorail(10))
    print(factorail._doc_)