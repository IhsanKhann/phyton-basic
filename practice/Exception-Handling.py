#Exception
#Types of Exception and handling exceptions
#Keywords:
  #else, finally, try, except, raise
#custom Exceptions
#multiple Exceptions

#A custom exception:
#Raise a Exception:
def check_Positive_Number(number):
  if number < 0:
    raise ValueError("Number not Positive.")
  return num

class InvalidAgeError(Exception):
  def __init__(self,message):
    self.message = message
    super().__init__(message)

def CheckAge(age):
  if age < 18:
    try:
      InvalidAgeError("Age below 18")
    except InvalidAgeError as e:
      print(e)
    return False

  return True

Age = int(input("Enter Age:"))
Verification = CheckAge(Age)

if(Verification):
  print("Your Allowed")
else:
  print("Your not Allowed") 

  
  try:
    print(check_Positive_Number(-5))
  except Exception as a:
    print(a)
  