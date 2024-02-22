def anagram(a, b):
    if len(a) == len(b) and sorted(a) == sorted(b):
        print("Anagram")
    else:
        print("Not an Anagram")


anagram("silent", "listen")

