def change_color(color):
  if color == "red":
    return ("\033[31m")
  elif color == "green":
    return ("\033[0;32m")
  elif color == "purple":
    return ("\033[0;35m")
  elif color == "blue":
    return ("\033[0;34m")
  elif color == "blue":
    return ("\033[0;34m")
  elif color == "yellow":
    return ("\033[33m")
  else:
    return ("\033[0m")
    
print("INTERFACE 1")
title = f"{change_color('red')}={change_color('reset')}={change_color('blue')}= {change_color('yellow')} Music App {change_color('reset')}={change_color('reset')}={change_color('red')}="

prev = "prev"
next = "next"
pause = "pause"

print(f"          {title:^35}")
print(f"🔥▶️\t{change_color('reset')}Radio Gaga")
print(f"\t{change_color('yellow')}Queen")
print()
print(f"{change_color('reset')}{prev:<35}")
print(f"{change_color('green')}{next:^35}")
print(f"{change_color('purple')}{pause:>35}")
print()
change_color('reset')

print(f"{change_color('reset')}INTERFACE 2")
text = "WELCOME TO"
print(f"{text:^35}\n")
text = "-- ARMBOOK --"
print(f"{change_color('blue')}{text:^35}\n")
text = "Definitely not a rip off of "
print(f"{change_color('yellow')}{text:>35}")
text = "a certain other social"
print(f"{text:>35}")
text = "networking site."
print(f"{text:>35}\n")
text = "Honest."
print(f"{change_color('red')}{text:^35}\n")
text = "Username:"
print(f"{change_color('reset')}{text:^35}")
text = "Password:"
print(f"{text:^35}")

