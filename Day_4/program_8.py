check_case=input("Enter the sentence:")  
up=[]
low=[]
for letter in check_case:
  if letter.isupper():
    up.append(letter)
  elif letter.islower():
    low.append(letter)
print("UPPER CASE:",len(up))
print("LOWER CASE:",len(low))
