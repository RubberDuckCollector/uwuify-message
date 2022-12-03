from random import randint

addOn = randint(1, 10)
if addOn == 1:
  addOn = "OwO"
elif addOn == 2:
  addOn = "UwU"
elif addOn == 3:
  addOn = "(人◕ω◕)"
elif addOn == 4:
  addOn = "(｀へ´)"
elif addOn == 5:
  addOn = "._."
elif addOn == 6:
  addOn = "^-^"
elif addOn == 7:
  addOn = "( ͡° ᴥ ͡°)"
elif addOn == 8:
  addOn = "(• o •)"
elif addOn == 9:
  addOn = "0w0"
elif addOn == 10:
  addOn == ". . .OwO, what's this. . .?"

msg = input("enter message: ")
msg = msg.replace("l", "w")
msg = msg.replace("r", "w")
msg = msg.replace("L", "W")
msg = msg.replace("R", "W")

print(msg + " " + addOn)