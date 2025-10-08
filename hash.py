def is_unique_chars(s: str) -> bool:
    # Assume ASCII (128 unique chars)
    if len(s) > 128:
        return False
    
    char_set = [False] * 128
    print(char_set)
    for ch in s:
        val = ord(ch)
        print(ch, val)# get ASCII code
        if char_set[val]:        # already seen?
            return False
        char_set[val] = True
    return True

# Tests
print(is_unique_chars("abc"))     # True
print(is_unique_chars("hello"))   # False
print(is_unique_chars(""))