# RegEx can be used to check if a string contains the specified search pattern.

## RegEx Module
import re

# Syntax: re.search(pattern, string, flags=0)

txt = "The rain in Spain"
# Search the string to see if it starts with "The" and ends with "Spain":
x = re.search("^The.*Spain$", txt)

if x:
  print("Yes, there is a match!")
else:
  print("No match")


## Metacharacters: . ^ $ * + ? {} [] | () \

# . - Any character except newline
# ^ - Starts with
# $ - Ends with
# * - Zero or more occurrences
# + - One or more occurrences
# ? - Zero or one occurrence
# {n} - Exactly n occurrences
# {n,} - n or more occurrences
# {n,m} - Between n and m occurrences
# [] - Matches any character in brackets
# [^] - Matches any character not in brackets
# | - Either or
# ( ) - Grouping
# \ - Escape special characters


## Special Sequences: \A \Z \b \B \d \D \s \S \w \W

# \A - Matches only at the start of the string
# \Z - Matches only at the end of the string
# \b - Matches a word boundary
# \B - Matches a non-word boundary
# \d - Matches a digit
# \D - Matches a non-digit
# \s - Matches a whitespace character
# \S - Matches a non-whitespace character
# \w - Matches a word character
# \W - Matches a non-word character


## Sets: [arn] [a-n] [^arn] [0123] [0-9] [0-5][0-9] [a-zA-Z] [a-zA-Z0-9] [+]

# [arn] - Matches any of the characters in the brackets
# [a-n] - Matches any character between a and n
# [^arn] - Matches any character not in the brackets
# [0123] - Matches any of the characters 0, 1, 2, 3
# [0-9] - Matches any digit
# [0-5][0-9] - Matches any two-digit number
# [a-zA-Z] - Matches any letter
# [a-zA-Z0-9] - Matches any letter or digit
# [+] - Matches one or more occurrences of the previous item


## The "findall()" Function
# Returns a list containing all matches
txt = "The rain in Spain"
x = re.findall("ai", txt)
print('\nfindall() function:',x)  # ['ai', 'ai']


## The "search()" Function
# Returns a Match object if there is a match anywhere in the string
txt = "The rain in Spain"
txt2 = "The first white-space charater is at position:"

x = re.search('\s', txt)

print('\nsearch() function:')
print(txt2, x.start()) # The first white-space charater is at position: 3


## The "split()" Function
# Splits the string at the matches and returns a list
txt = "The rain in Spain"
x = re.split("\s", txt)
print('\nsplit() function:',x)  # ['The', 'rain', 'in', 'Spain']

# E.g. Split the string only at the first occurrence:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)  # ['The', 'rain in Spain']


## The "sub()" Function
# Replaces the matched pattern in the string with a new pattern
txt = "The rain in Spain"
x = re.sub("\s", " | ", txt)
print('\nsub() function:',x) # The | rain | in | Spain

# E.g. Replace the firt 2 occurrences:
txt = "The rain in Spain"
x = re.sub("\s", " | ", txt, 2)
print(x) # The | rain | in Spain


## Match Object
# Is an object containing information about the search and the result.

# E.g. Do a seach that will return a match object:
txt = "The rain in Spain"
x = re.search("ai", txt)
print('\nMatch Object:',x) # Match Object: <re.Match object; span=(4, 5), match='ai'>


## Match Object Attributes:
txt = "The rain in Spain"
# The regular expression looks for any words that starts with an upper case "S".

# ".span()" - Returns a tuple containing the start and end indexes of the match.
x = re.search(r"\bS\w+", txt)
print('Span Attribute:',x.span()) # (12, 17)

# ".string" - Returns the string passed into the function
x = re.search(r'\bS\w+', txt)
print('String Attribute:',x.string) # The rain in Spain

# ".group()" - Returns the part of the string where there was a match
x = re.search(r'\bS\w+', txt)
print('Group Attribute:',x.group()) # Spain