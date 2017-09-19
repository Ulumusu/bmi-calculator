import sys #import sys because i need to quit


def check(z): #check Your weight and give final answer
  if z<16:
    print("Starvation!!!!")
  elif 16<z<16.99:
     print("Emaciation!!!!")
  elif 17<=z<=18.49:
     print("Underweight!!!")
  elif  18.5<=z<=24.99:
     print("OK")
  elif 25<=z<=29.99:
     print("Overweight!!!")
  elif 30<=z<=29.99:
     print("You are FAT!!!")  
  again=input("Do you want check again??\n(1) yes\n(2) no\n(number please) ")
  if again=="1":
    main_menu()
  elif again=="2":
    print("Goodbye")
    sys.exit()
    

def BMI_calculator(x, y): #BMI calculator
  result=(x/(y**2))
  print("Your BMI: %d" %(result))
  check(result)
  

def main_menu():
  print("Welcome in BMI calculator.")
  height=float(input("Please give me the height: "))
  weight=float(input("Please give me the weight: "))
  BMI_calculator(weight, height)
  
main_menu()  