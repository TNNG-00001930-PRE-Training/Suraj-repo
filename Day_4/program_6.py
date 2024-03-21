def duplicate_strings(s):
    s=list(s.split())
    s=set(s)
    k=sorted(list(s))
    return " ".join(k)
s=input("Enter the words by using white as a seperator:")
print(duplicate_strings(s))