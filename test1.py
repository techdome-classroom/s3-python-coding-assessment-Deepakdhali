def isValid(s: str) -> bool:
    # Stack to keep track of opening brackets
    stack = []
    
    # Hash map to keep mappings of closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    # Traverse each character in the string
    for char in s:
        if char in bracket_map:
            # Pop from stack or use a default invalid character
            if not stack or stack.pop() != bracket_map[char]:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
    
    # In the end, if the stack is empty, the string is valid
    return not stack

# Test cases
print(isValid("()"))       # True
print(isValid("()[]{}"))   # True
print(isValid("(]"))       # False
print(isValid("([)]"))     # False
print(isValid("{[]}"))     # True
