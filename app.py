# paste this in input for testing -> yo “heheh“ they said
string_sanitizer = input("Paste string here: ")
print(string_sanitizer)
if "“" in string_sanitizer:
    sanitized_string = string_sanitizer.replace("“", "\"")
    print(sanitized_string)