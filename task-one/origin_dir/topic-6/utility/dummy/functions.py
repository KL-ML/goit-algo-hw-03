from utility import nice_function


def not_bad(s: str) -> str:
    if s.find("not") == -1 or s.find("bad") == -1:
        print(nice_function())
        return s
    else:
        return s.replace("not bad", "good")
