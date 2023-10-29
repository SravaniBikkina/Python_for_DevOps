#String Concantetion
str1 = "DevOps"
str2 = "Engineer"
Result = str1+ " " +str2
print(Result)
#For length of the string
Text = "DevOps Engineer"
Length = len("DevOps Engineer")
print("Lenght of the string =", Length)
#Lower and Upper case
Text = "DevOps Engineer"
uppercase = Text.upper()
lowercase = Text.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
#To replace text
Text = "DevOps Eng"
New_text = Text.replace("Eng", "Engineer")
print("modified text:", New_text)
#Split text
Text = "DevOps engineer"
words = Text.split()
print("Words:", words)
#Stripped text
text = "   DevOps engineer   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)
#Sub string
Text = "DevOps engineers are"
substring = "are"
if substring in text:
    print(substring, "found in the text")

#Integers and float
# Integer variables
num1 = 13
num2 = 5

# Integer Division
result1 = num1 // num2
print("Integer Division:", result1)

# Modulus (Remainder)
result2 = num1 % num2
print("Modulus (Remainder):", result2)

# Absolute Value
result3 = abs(-7)
print("Absolute Value:", result3)

# Float variables
num1 = 1.2
num2 = 2.5

# Basic Arithmetic
result1 = num1 + num2
print("Addition:", result1)

result2 = num2 - num1
print("Subtraction:", result2)

result3 = num1 * num2
print("Multiplication:", result3)

result4 = num1 / num2
print("Division:", result4)

# Rounding
result5 = round(3.14159265359, 2)  # Rounds to 2 decimal places
print("Rounded:", result5)


#Regular expression

import re

text = "The quick brown fox"
pattern = r"quick"

match = re.findall(pattern, text)
if match:
    print("Match found:", match)
else:
    print("No match")
#Replacement
import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)

#Replace
import re

text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)
