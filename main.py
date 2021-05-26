# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
# For Love Scores **less than 10** or **greater than 90**, the message should be:

# `"Your score is **x**, you go together like coke and mentos."` 

# For Love Scores **between 40** and **50**, the message should be:

# `"Your score is **y**, you are alright together."`

# Otherwise, the message will just be their score. e.g.:

# `"Your score is **z**."`

#Write your code below this line 👇
combine_names = name1 + name2
combine_names_true = combine_names.lower().count('t') + combine_names.lower().count('r') + combine_names.lower().count('u') + combine_names.lower().count('e')
combine_names_love = combine_names.lower().count('l') + combine_names.lower().count('o') + combine_names.lower().count('v') + combine_names.lower().count('e')
score = int(str(combine_names_true) + str(combine_names_love))
if score < 10 or score > 90:
  print(f'your score is {score}, you go together like coke and mentos.')
elif score >= 40 and score <= 50:
  print(f'your score is {score}, you are alright together.')
else:
    print(f'your score is {score}')


