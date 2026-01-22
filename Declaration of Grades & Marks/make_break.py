print("The Verdict: Pass or Fail\n\n")

passing_score = 50

my_score = int(input("Enter your score(0-100):"))

if (my_score>=passing_score and my_score<=100):
    print("Congratulations on passing the exam.")

elif(my_score>100):
    print("Your marks should be under 100!")

else:
    print("You failed, try harder next time.")
