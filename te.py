def is_float(string):
    try:
        float(string)
        if '.' in string:
            return True
        else:
            return False
    except ValueError:
        return False

# Test
print(is_float("3.14"))   # Output: True
print(is_float("3.14.5")) # Output: False
print(is_float("3"))      # Output: False
