# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# t1 = name1.lower().count("t")
# r1 = name1.lower().count("r")
# u1 = name1.lower().count("u")
# e1 = name1.lower().count("e")
# l2 = name2.lower().count("t")
# o2 = name2.lower().count("r")
# v2 = name2.lower().count("u")
# e2 = name2.lower().count("e")
# total = t1 + r1 + u1 + e1 + l2 + o2 + v2 + e2

# t3 = name1.lower().count("l")
# r3 = name1.lower().count("o")
# u3 = name1.lower().count("v")
# e3 = name1.lower().count("e")
# l4 = name2.lower().count("l")
# o4 = name2.lower().count("o")
# v4 = name2.lower().count("v")
# e4 = name2.lower().count("e")
# total2 = t3 + r3 + u3 + e3 + l4 + o4 + v4 + e4

# Shorter ver. using string concatenation
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

# love_score = (str(total) + str(total2))

if (love_score) < 10 or (love_score) > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score) <=50 and (love_score) >= 40:
  print(f"Your love score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")