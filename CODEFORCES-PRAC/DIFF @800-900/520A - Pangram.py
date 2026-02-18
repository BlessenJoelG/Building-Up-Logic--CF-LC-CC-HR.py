t = input()
chk = set()
text = input()
text = text.lower()
for char in text:
    if "a"<= char <="z":
        chk.add(char)
if len(chk) == 26:
    print("YES")
else:
    print("NO")