import re 

user_password = input ("Please create a password: ")
user_password2 = input ("Please re-enter you password: ")

if user_password != user_password2 : 
  print("Invalid! These passwords don't match.")

while user_password == user_password2:
  if len(user_password2) <6 :
    print("Invalid! Password must be more than 6 characters.")
  break
  if len(user_password2) >20:
    print("Invalid! Password must be less than 20 characters.")
  break

x = True
while x :

  if not re.search("[a-z]", user_password2):
    print("Invalid! Password must contain at least one lowercase letter!")
    break
  elif not re.search("[0-9]", user_password2):
    break
  elif not re.search("[A-Z]", user_password2):
    break
  elif not re.search("[$#@!]", user_password2):
    break

  else:
        print("This is a strong password!")
        x=False
        break

if x:
    print("This is a weak password!")
