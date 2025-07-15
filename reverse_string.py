def reverse_string(s):
    if len(s) == 0:
        return ""
    else:
        return reverse_string(s[1:]) + s[0]

# Example usage:
input_string = input("Enter a string to reverse: ")
print("Reversed string:", reverse_string(input_string))