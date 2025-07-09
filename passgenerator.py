import random
import string

def generate_password(length):
  
  char = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(char) for i in range(length))
  return password

try:
  password_length = int(input("Enter the desired password length: "))
  if password_length <= 0:
    print("Password length must be a positive integer.")
  else:
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)
except ValueError:
  print("Invalid input. Please enter a valid integer for the password length.")
