temp = 16
msg = " "

if temp  < 0:
    msg = "cold"
elif temp < 10:
    msg = "Mild"
elif temp < 20:
    msg = "Good"
elif temp < 30:
    msg = "Hot"
else:
    msg = "Hell"
print(msg)

msg = "Let's play" if temp > 15 else "stay home"
print(msg)