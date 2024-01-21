def question(i):
    print("\nHere comes your next question of",money[i],"rupees\n\n")
def crct():
    print("Congratulations You are right ",call2,name,"and you have won",money[i],"rupees",call1)
    win=money[i]
    if win==money[4] or win==money[9]:
       print("You have entered safe check point")
    return i+1
def done():
   print("Thanks for coming to our show",call2,name,"All the best for your future",call1)
   exit()
def answer():
   a=int(input("Enter your answer in integer from 1-4 or enter 0 to quit\n"))
   while a>4 or a<0:
    print("Error entered . Please check your option again:")
    a=int(input("Enter your answer in integer from 1-4 or enter 0 to quit\n"))
   return a 

def check(right):
    if q1==right:
     z=crct()
    elif q1==0 and money[i]<=money[4]:
     print("You have quit the game\nYou have won nothing")
     done()
    elif q1==0 and money[i]>=money[4]:
     print("You have quit the game\nYou have won",money[i-1],"rupees")
     done()
    else:
     win=money[i-1]
     if win>=0 and win<money[4]:
        print("You are wrong and You have won 0 rupees\n I feel sorry for you")
        done()
     elif win>=money[4] and win<money[9]:
        print("You are wrong and You have won 10000 rupees\n I feel sorry for you")
        done()
     elif win>=money[9]:
        print("You are wrong and You have won 320000 rupees\n I feel sorry for you")
        done()
    return z
money=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
solutions=[4,3,2,1,3,4,3,1,1,3,4,4,3,1,1]
Questions = [
    "Q1: Who was the Player of the Tournament when India won the World Cup in 2011?\nYour options are\n opt1=\"Gambhir \", opt2=\"Sachin \", opt3=\"Sehwag \", opt4=\"Yuvraj \"",
    "Q2: Can u name the team which has Qualified the least number of times in IPL?\nYour options are\n opt1=\"DELHI \", opt2=\"bangalore \", opt3=\"punjab \", opt4=\"Rajasthan \"",
    "Q3: Which Indian Cricket Stadium has the largest Capacity?\nYour options are\n opt1=\"Wankhede, Mumbai\", opt2=\"Motera, Ahmedabad\", opt3=\"Chepauk, Chennai \", opt4=\"Uppal, Hyderabad \"",
    "Q4: What is the name of the Award for the leading wicket Taker in the ICC World Cup?\nYour options are\n opt1=\"Golden ball award\", opt2=\"Golden wicket award\", opt3=\"Platinum ball award \", opt4=\"Platinum wicket award\"",
    "Q5: Who is the only person on this planet to score 50 ODI centuries?\nYour options are\n opt1=\"Sachin Tendulkar\", opt2=\"Ricky ponting\", opt3=\"Virat Kohli \", opt4=\"Michael Clarke\"",
    "Q6: First Indian player to get the Title “Man of the Tournament” in the ICC World Cup?\nYour options are\n opt1=\"Kapil Dev\", opt2=\"Ganguly\", opt3=\"Sunil Gavaskar\", opt4=\"Sachin Tendulkar\"",
    "Q7: At any one time, how many players on a cricket field can wear gloves?\nYour options are\n opt1=\"1\", opt2=\"2\", opt3=\"3 \", opt4=\"4 \"",
    "Q8: Which country hosted the first ICC world cup?\nYour options are\n opt1=\"England\", opt2=\"West Indies\", opt3=\"Australia \", opt4=\"India\"",
    "Q9: Which batsman among the following has the best test average?\nYour options are\n opt1=\"Sachin\", opt2=\"Sehwag\", opt3=\"Dravid\", opt4=\"Gavakasar\"",
    "Q10: How long was the Longest Test Match in History?\nYour options are\n opt1=\"5 days\", opt2=\"7 days\", opt3=\"9 days\", opt4=\"10 days \"",
    "Q11: With which Country did India play its First Test Match?\nYour options are\n opt1=\"Australia\", opt2=\"West Indies\", opt3=\"Pakistan \", opt4=\"England \"",
    "Q12: Which cricketer scored the first triple century?\nYour options are\n opt1=\"Sehwag\", opt2=\"Ian Chappell\", opt3=\"Don Bradman \", opt4=\"Andy Sandham \"",
    "Q13: Who among the following is the first Indian bowler to take a wicket?\nYour options are\n opt1=\"Bapu Nadkarni\", opt2=\"Imran Khan\", opt3=\"Mohammad Nissar \", opt4=\"Vyanktesh Prasad\"",
    "Q14: Who recorded the first hat-trick in a Test Match?\nYour options are\n opt1=\"Harbhajan Singh\", opt2=\"Kapil dev\", opt3=\"Bapu Nadakarni\", opt4=\"Chetan Sharma \"",
    "Q15: Prior to Sachin Tendulkar scoring his double century, which player jointly held the record for the highest score in ODIs with Saeed Anwar?\nYour options are\n opt1=\"Charles Coventry\", opt2=\"Viv Richards\", opt3=\"Zaheer Abbas \", opt4=\"David Gower\"",
]
#START
print(len(Questions))
print("WELCOME TO KAUN BANEGA KARODPATHI\n Here is your BIGB AMITABH BACHCHAN WITH YOU")
i=0
name=input("Please tell ur good name:")
age=int(input("Please tell your age:"))
place=input("Where do u live:")
gender=input("M or F or OTHER:")
if gender=="M":
    call1="sir"
    call2="Mr."
else:
    call1="mam"
    call2="Mrs."

print("OK!!HEARTY WELCOME TO U",call2,name,"TO KBC")
print("Coming from a Great place like ",place,",Its good to meet u",call1)
print(f"OK NOW LETS DIVE INTO THE GAME \nHere comes your first question of 1000 rupees\n{name}")
#gamebegins
for i in list(range(16)):
    print(Questions[i])
    q1=answer()
    right=solutions[i]
    if i==0:
     win=0
    next=check(right)
    if i!=14:
     question(next)
    else:
     print("You are awesome . You have won 1 crore and you are Karodpathi , Koteeswarudu and What Not",call1,"\n",call2,name,"You are simply amazing\n","Take this cheque of 1 crore")
exit()
