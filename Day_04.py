Play = True
while (Play):

    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''
    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''
    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    print(rock + paper + scissors)
    
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    chosen = ['Rock', 'Paper', 'Scissors']
    print("\n")

    print("Your choice is : " + chosen[user_choice])

    import random
    lap_choice = random.randint(0,2)
    choose = ['Rock', 'Paper', 'Scissors' ]
    print("A.I's choice is :" + choose[lap_choice])

    print("\n")

    if user_choice > 2 or user_choice < 0 :
        print("Invalid Selection of Choice !")
    elif user_choice == lap_choice :
        print("Draw !")
    elif user_choice == 0 and lap_choice == 2:
        print("You Lost from AI !")
    elif user_choice == 2 and lap_choice ==0:
        print("You won bro !")
    elif user_choice > lap_choice :
        print("You won bro !")
    elif user_choice < lap_choice:
        print("You Lost from AI !")

    print("\n\n")
    again = input("Do you want to play again ?Y or N").upper()
    if again == "N":
        break
