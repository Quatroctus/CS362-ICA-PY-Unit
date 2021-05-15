
def is_palidrome(s:str) -> bool:
    s = s.replace(" ", "").replace("-", "").lower()
    return s == s[::-1]
