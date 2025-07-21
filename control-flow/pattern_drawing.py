pattern_size = int(input("Enter the size of the pattern: "))

x = pattern_size

while x > 0:

    x -= 1

    for size in range(pattern_size):
        print("*", end="")

    print("")
        
    
    