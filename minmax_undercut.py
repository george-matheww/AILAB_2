from random import randrange
A_score=0
B_score=0
counter=1
while (A_score<100 and B_score<100):
    print("Round",counter)
    A_choice=randrange(1,6)
    print("A chooses:",A_choice)
    B_choice=randrange(1,6)
    print("B chooses:",B_choice)
    if ((A_choice-B_choice)==1):
        B_score+=B_choice+A_choice
    elif ((B_choice-A_choice)==1):
        A_score+=A_choice+B_choice
    else:
        A_score+=A_choice
        B_score+=B_choice
    print("A score is:",A_score)
    print("B score is:",B_score)
    print("\n")
    counter+=1
if (A_score>=100):
    print("A is the winner with score",A_score)
elif(B_score>=100):
    print("B is the winner with score",B_score)
else:
    print("A and B end in a draw")