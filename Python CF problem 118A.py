I=input("")

V=("a","e","i","o","u","y")

if I.isalpha():
  for i in I:
    if i.lower() in V:
      continue
    else:
      print("."+i.lower(), end="")
else:
  print("Invalid Input\nProgram terminated")