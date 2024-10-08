def romanToInt(s: str) -> int:
    # Map to convert Roman numerals to integers
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    total = 0
    n = len(s)
    
    for i in range(n):
        # Check if we should subtract the current numeral (based on subtractive rules)
        if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
            total -= roman_map[s[i]]
        else:
            total += roman_map[s[i]]
    
    return total

# Test cases
print(romanToInt("III"))      # 3
print(romanToInt("LVIII"))    # 58
print(romanToInt("MCMXCIV"))  # 1994
print(romanToInt("IV"))       # 4
print(romanToInt("CDXLIV"))   # 444
print(romanToInt("MMMCMXCIX"))  # 3999 - maximum valid Roman numeral
print(romanToInt("IM"))       # Invalid input (incorrect Roman numeral, would return an incorrect value if allowed)
