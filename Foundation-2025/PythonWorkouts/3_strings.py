text = "Hello, St' Peter church!"
print(text)
print(text.upper())
print(text.lower())

another_text = "another \"text\"" # escaping unsupported special char
print(another_text)

another_text = 'another "text"'
print(another_text)

print("two \nlines")

multiline_text = """
This is
a multiline
text
"""
print(multiline_text)


# Formatted strings or F-String
var = "text"
new_string = f"1 {var} 2 - { 1+ 5}"
print(new_string)

