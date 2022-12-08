#Lousiane Gauthier
#This Python program displays a golf score card and
# It also,lets you fill your score for each hole,
#and calculates your stadistics of your round
#Sources: W3Schools, https://www.w3schools.com/python/python_intro.asp

#Function definitions:
#Menu
def menu():
    print("Hello! Welcome to your golf score card!")
    print("----------------Menu-------------------")
    print("1. Fort Myers Country Club")
    print("2. Shadow Wood Country Club")
    print("3. Gateway Country Club")
    
#score card
def score_card():
    print("Hole",end="")
    for firstNine in range(0,9):
        print(" |",firstNine+1,end="")
    print(" |Out",end="")
    for secondNine in range(0,9):
        print(" |",secondNine+1,end="")
    print(" |In|Total|")

#Menu input
def exceptions_menu():
    error="Invalid character. Try again"
    flag=False
    print("Which course are you playing today?")
    
    #Try-Except for invalid user input
    while flag==False:
        try:
            course=int(input("Enter a number:"))
            if (course<1) or course>3:#conditional operator
                print(error)
                flag=False
            else:
                flag=True
        except:
            print(error)
    #Conditional execution depending on the par of the golf course
    if course==1:
        par=71
    elif (course==2) or (course==3):#Logical operator 
        par=72
    #Returning value to be able to use it outside this function
    return(par)

#Control of invalid user input
def errors_control(promt):
    x=False
    while x==False:
        try:
            userInput=int(input(promt))
            x=True
        except:
            print("That was not a valid number. Please try again.")
            x=False
    return(userInput)

           
#User hole input and print of user score card
def holes_input():
    sumFirst9=0
    sumSecond9=0
    promt="Enter the score for hole "
    #A list for the score of each hole
    first_nine=[0,0,0,0,0,0,0,0,0,0]
    second_nine=[0,0,0,0,0,0,0,0,0,0]
    print("Enter your score for each hole and press enter")

    #Range function
    #Filling up the list
    for x in range (0,9):
        holeNumberIn=str(x+1)
        promt2=promt+holeNumberIn+": "
        first_nine[x]=errors_control(promt2)
        #Sum of first nine holes
        sumFirst9+=first_nine[x] #Shortcut operator +=
        
    for y in range (0,9):
        holeNumberOut=str(y+10)
        promt2=promt+holeNumberOut+": "
        second_nine[y]=errors_control(promt2)
        #Sum of second nine holes
        sumSecond9+=second_nine[y] 

    total=sumFirst9 + sumSecond9
    
    #Show score card
    score_card()
    
    #Print User Score
    print("    ",end="")
    for x in range (0,9):
        print(" |",first_nine[x],end="")
    print(" |",sumFirst9,end="")
    for y in range (0,9):
        print(" |",second_nine[y],end="")
    print(" |",sumSecond9,"|",total,"|")

    return(total)

#Function def with parameters
def handicap_calculation(total1, par1):
    handicap1=total1-par1
    return(handicap1)

#Function print and calculate stadistics of your round of golf
def stats(total,par):
    handicap=handicap_calculation(total,par)
    mean=total/18 #total=18holes score
    #Time of play
    promt="How many minutes did your round took? "
    minutes_playing=errors_control(promt)
    #Numeric operator, hole part of the division
    hours=minutes_playing//60
    #Numeric operator, remainder of the division
    minutes=minutes_playing%60
    #Numeric operator, division with its decimal part
    mean_minutes= minutes_playing/18 
    if minutes_playing>=280:
        time_playing=("you played really slow, keep up the next time!")
    #using relational operation != (different)
    elif (minutes_playing!=280) and (minutes_playing<280): 
        time_playing=("Congratulations! "*3)
    #show stats
    print("Today you played a handicap of:",handicap,".")
    print("You score an average of",format(mean,'.1f'),"shots per/hole.")
    print("Your round took",hours,"hours and",minutes,end="")
    print(" minutes, an estimated of",format(mean_minutes,'.1f'),end="")
    print(" min/hole",time_playing,"\n")
    
#Main function definition:
def main():
    
    #Function calls
    menu()
    
    #This step is necessary for the later calculation of the handicap
    #User input option from menu
    par=exceptions_menu()
        
    score_card()
    
    total=holes_input()

    stats(total,par)

    print("END OF THE PROGRAM")

#FUNCTION CALL MAIN
main()    
  
#numeric operators that I did not use in my program but where require.
#multiplication
multiplication=2*32
#exponents, 2 to the power of 3, 2x2x2=8
exponents= 2**3
divisible=False
#Boolean Operator not
if not(exponents%2!=0 and multiplcation%2!=0):
    divisible=True


    
    
    
    
        

    

    
    
    


    


    


