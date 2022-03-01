guess_number=9
guess_count=0
guess_limit=3
while guess_count< guess_limit:
    guess=int(input("Enter The Guess Number from 0 to 10 : "))
    guess_count +=1
    if guess==guess_number:
        print("You Won")
        break
    else :
        print("Sorry,You Lost")