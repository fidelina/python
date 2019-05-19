def count_symbol(s: str, x: str) -> int:
    count = 0
    for i in range(0, len(s)):
        if s[i] == x:
            count += 1
    return count


print(count_symbol("   String str lol trololo   ", " "))
