
"""
Lab 3.3 – Operator Frequency Counter

Goals:
- Practice using strings and dictionaries.
- Count character frequencies in user-provided text.
"""


expression = input("Enter an arithmetic expression: ")


operators = ['+', '-', '*', '/', '(', ')']


operator_counts = {op: 0 for op in operators}


for char in expression:
    if char in operators:
        operator_counts[char] += 1


print("Operator counts:", operator_counts)
