




def add():
    x=25
    y=76
    z=x+y
    return z

def multiply():
    
    b = 3 * add()
    return b

def main():
    addi=add()
    multi=multiply()
    print(f"adddition: {addi}")
    print(f"multiply: {multi}")


if __name__ == "__main__":
    main()