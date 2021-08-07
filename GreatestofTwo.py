# Greatest of two values
# Def the value of X
X = float(input("Please enter the value of X :"))
# Def the value of Y
Y = float(input("Please enter the value of Y :"))
# Set the value of Counter to 0(it is used to see how many times the loop executed)
Counter = 0
# Used if else and elseif and while
if X == Y:
    print("X and Y are equal")
elif X > Y:
    print("X and Y are not equal")
    while X > Y:
        Counter += 1
        Y += 1
        print("Y is incremented to ", Y)
        if X == Y:
            print("After Incremented Y value", Counter, ' times ', ", Inputs are equal")

else:
    print("Y is bigger")
    while Y > X:
        Counter += 1
        X += 1
        print("X is incremented to ", X)
        if X == Y:
            print("After Incremented X value", Counter, ' times ', ", Inputs are equal")
