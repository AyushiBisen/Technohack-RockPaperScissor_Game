import random
print("\n****** Welcome to Rock,Paper,Scissors Game ******")

user_score= 0
comp_score= 0
ties= 0

name= input("\nEnter your name here: ")
print("""
     Winning Rules:
     1.Rock Vs Scissors --> Rock
     2.Paper Vs Scissors --> Scissors 
     3.Paper Vs Rock --> Paper""")

while True:
     
     print("""
          Choices are:
          1.Rock
          2.Paper
          3.Scissor""")
     choice=int(input("Enter your choice from 1 to 3: "))
     print()
     while choice> 3 or choice< 1:
          choice=int(input("Enter Valid Choice!"))
          
     if choice==1:
          user_choice= "Rock"
     elif choice==2:
          user_choice= "Paper"
     else:
          user_choice= "Scissor"     
          
     print("The user's choice is",user_choice)     
     print("\nNow it is Computer's turn!")

     computer= random.randint(1,3)
          
     if computer==1:
          comp_choice= "Rock"
     elif computer==2:
          comp_choice= "Paper"
     else:
          comp_choice= "Scissor"     
          
     print("The Computer's choice is",comp_choice)       

     if((user_choice=="Paper" and comp_choice=="Rock") or (user_choice=="Rock" and comp_choice=="Paper")):
          print("Paper wins!!")
          result= "Paper"          
     elif((user_choice=="Scissor" and comp_choice=="Rock") or (user_choice=="Rock" and comp_choice=="Scissor")):
          print("Rock wins!!")
          result= "Rock"   
     elif((user_choice==comp_choice)):
          print("Its a Tie!!")
          result= "tie"  
          
     else:
          ("Scissor Wins!!")   
     result= "Scissor"    
     
     
     if result== "tie":
          ties += 1
     elif result== user_choice:
          user_score += 1
          print("User wins!!")
     else:
          comp_score += 1 
          print("Computer wins!!")    
                    
     print("Scores are:")
     print(name,"'s score is", user_score)
     print("Computer's score is", comp_score)    
     print("Ties are:",ties)           
     
     repeat = input("Do you want to play again?")
     if repeat == "no" or  repeat=="No":
      break
 
print("Game over!")
print("Thanks for playing.")
 