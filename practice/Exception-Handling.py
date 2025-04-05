#Exception
#Types of Exception and handling exceptions
#Keywords:
  #else, finally, try, except, raise
#custom Exceptions
#multiple Exceptions

#A custom exception:
#Raise a Exception:
# def check_Positive_Number(number):
#   if number < 0:
#     raise ValueError("Number not Positive.")
#   return num

# class InvalidAgeError(Exception):
#   def __init__(self,message):
#     self.message = message
#     super().__init__(message)

# def CheckAge(age):
#   if age < 18:
#     try:
#       InvalidAgeError("Age below 18")
#     except InvalidAgeError as e:
#       print(e)
#     return False

#   return True

# Age = int(input("Enter Age:"))
# Verification = CheckAge(Age)

# if(Verification):
#   print("Your Allowed")
# else:
#   print("Your not Allowed") 

  
#   try:
#     print(check_Positive_Number(-5))
#   except Exception as a:
#     print(a)
  
#Tasks on raise:
# def CheckNegativeNumber(num):
#   if num < 0:
#     raise ValueError("Negative Number. Error.")
#   return num  

# try:
#   print("Number is: ", CheckNegativeNumber(-21))
# except ValueError as a:
#   print(a)

# #Task-2:
# class NegativeError(Exception):
#   def __init__(self,message):
#     self.message = message 
#     super().__init__(message) #single parameter provokes the Exception class Constructor

# def CheckAge(Age):
#   if Age < 0:
#     raise NegativeError("Negative Input not allowed.")
#     return Age 
#   else:
#     return Age

# try:
#   print("Age is: ",CheckAge(20))
# except NegativeError as E:
#   print(E) 

# #Task-3:
# def DivideNum(a,b):
#   result = 0
#   if a and b > 0:
#     result = a/b
#     return result
#   else:
#     raise ZeroDivisionError("Cannot Divide by zero.")
#   return result

# try:
#   print(DivideNum(10,0))
# except ZeroDivisionError as E:
#   print(E)

# #Task4:
# # Raise exception with a specific condition
# # Create a function that accepts a string as input.
# # If the string contains any digits, raise a ValueError
# # and provide a message like "Input cannot contain digits."

# def TakeInput(input="None"):
#   result = ""
#   try:
#     for char in input:
#       if char.isdigit():
#         raise TypeError("Input cant have digits.")
      
#     result += input
#     print(result)
#   except TypeError as E:
#     print(E)

# TakeInput("10")
# TakeInput("Ihsan")

# # Task5:
# # Custom exception with attributes
# # Create a custom exception called InvalidAgeError.
# #  The exception should accept a message and an age
# #  parameter. In a function, raise this exception if
# #  the age is below 18, with a message like "Age cannot be
# #  below 18."

# class InvalidAgeError(Exception):
#   def __init__(self, message="None", age=None):
#     self.message = message
#     self.age = age
#     super().__init__(message, age)

#   def CheckAge(self, Age):
#     if Age < 18:
#       raise InvalidAgeError("Age cannot be below 18.", Age)
#     return Age

# age_checker = InvalidAgeError()

# try:
#   print(age_checker.CheckAge(20))  
#   print(age_checker.CheckAge(10))

# except InvalidAgeError as E: #name of the exception(class)
#   print(f"Error: {E}, Age: {E.age}")

# #Task-6:
# def DivideTheNum(a,b):
#   result = 0
#   if a > 0 and b > 0:
#     result = a/b
#     return result
#   else:
#     if b == 0:
#       raise ZeroDivisionError("Cant Divide by Zero")
#     else:
#       raise ValueError("Error Occurred.")
#     return result

# try:
#   print(f" Result is { DivideTheNum(10,2) } ")
# except (ZeroDivisionError,ValueError) as E:
#   print(E)

#Task-7:
# def myFunction(num):
#   answer = 100
#   if num == 0:
#     raise ZeroDivisionError("Number cant be Divided by zero")  
#   return num

# #main:
# Result = 0
# num = 0
# try:
#   Answer = myFunction(num)
#   Result = Answer/num
# except ZeroDivisionError as E:
#   print(E)
#   raise

#Multiple Exceptions:
# def function1(num1,num2): 
#   result = 0
#   choice = input("Enter choice D/C: ").lower()
#   if choice == "d": #1st operation
#     if num1 > 0 and num2 > 0:
#       result = num1/num2
#       return result 
#     elif num2 == 0:
#       raise ZeroDivisionError("Num2 cant be zero.")
#   elif (choice == "c"):
#     try:
#       ConvertNum2 = str(num2)
#       if(num2 != 2):
#         raise ValueError("int cant be converted to string.")
#       else:
#         print("Successfully converted")
#     except:
#        raise ValueError("int cant be converted to string.")
#   else:
#     raise ValueError("wrong choice.")
  
#   return result 

# try: 
#   print(function1(10,2))
#   print(function1(10,0))
# except (ZeroDivisionError,ValueError) as e:
#   print("Error:", e)


# def function2(num1,num2,str_num):
#   result = 0
#   try:
#     result = num1/num2
#     print(f"Result is: {result}")
  
#     #2nd operation:
#     num2 = int(str_num)
#     print(f"String: {str_num} is converted: {num2}")

#   except ZeroDivisionError:
#     print("Cant be divided by zero.")
#   except ValueError:
#     print("couldnt be converted.")

#   return result 

# try:
#   print(function2(10,20,"20"))
#   print(function2(10,0,"20"))
# except (ZeroDivisionError, ValueError) as E:
#   print(E)

def function3(mylist):
  try:
    for i in mylist:
      if isinstance(i, str) and i.isdigit():  # Check if the element is a string and can be converted to a number
        raise TypeError("All data types are not the same.")
      elif i < 0:  # Check for negative numbers
        raise ValueError("Number can't be Negative.")
                
  except ValueError as ve:
    print(f"ValueError: {ve}")
  except TypeError as te:
    print(f"TypeError: {te}")
  except IndexError:  # This will not be needed here, but it's left in case we add checks for out-of-range indices later
    print("IndexError: Out of Index or list empty.")

# Main execution:
mylist = [10, 20, 3, -4, 12]  # Contains a negative number, so ValueError will be raised
mylist2 = ["20", 3, 10, 3, 40]  # Contains a string, so TypeError will be raised
mylist3 = list()  # Empty list, should not raise any exceptions

function3(mylist)
function3(mylist2)
function3(mylist3)

def function4(num1=0,num2=0):
  result = 0
  try:
    if num2 == 0:
      raise ZeroDivisionError("Zero is not allowed")
      return result
    elif num1 < 0:
      raise ValueError("Number is Negative.")
      return result 
    elif not isinstance(num1, (int,float)):
      raise TypeError("Number is not an int")
      return result
    else:
      result = num1/num2
      return result 
  except (ZeroDivisionError,ValueError,TypeError) as E:
    print("Error is: " , E)

  return result 
  
  
print(function4(10)) #zeroError
print(function4(-20)) #zeroError
print(function4(-20,10)) #ValueError
print(function4(10,"20")) #TypeError
print(function4(20,5)) #Nomral (NoError)

