print("Assess Your Marks - II")
my_marks = int(input("Enter the marks(0-100):"))

if (my_marks < 35):
    
  print("You are failed the exam.")
elif (my_marks >= 35 and my_marks < 60):
    
  print("Passed with B grade.")
elif(my_marks > 60 and my_marks <= 85):
    
  print("Passed with B grade.")
else:
    
  print("Passed wih A grade.")