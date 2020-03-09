# Task: print the lyrics for the song "99 Bottles of Beer"
# Note: Future Luna is probably going to bitch about this shit, but what does she know, she's an idiot.
for i in range(99):
    a = 99 - i
    if a > 2:
        bottles = "bottles"
        bottle = "bottles"
    elif a == 2:
        bottles = "bottles"
        bottle = "bottle"
    else:
        bottles = "bottle"
        bottle = "bottles"
    print(f"{a} {bottles} of beer on the wall")
    print(f"{a} {bottles} of beer")
    print("Take one down, pass it around")
    print(f"{a-1} {bottle} of beer on the wall\n")
