# A Man lost in forest , can come out if there press right
Counter = 0
print(Counter)
n = input("You are lost in the forest \n ********** \n ****************\n")
while (n == 'd') or (n == 'D'):
    Counter += 1
    n = input("Welcome to dark deep forest \n ******* What is your next turn ******")
    if Counter>5:print("your are in deep of hell \n ***:CJ****")
while (n == 'A') or (n == 'a'):
    Counter -= 1
    n = input("Welcome to dark deep forest \n ******* What is your next turn ******")
    print(Counter)
    if 0 == Counter:
        break
if Counter == 0:
    print("you are out")
