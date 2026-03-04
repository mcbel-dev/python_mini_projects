MIN_AGE = 1
MAX_AGE = 120

def validate_age(value):
    value = value.strip()
    
    if not value.isdigit():
        return "INVALID"
    
    age = int(value) 
    if age < MIN_AGE or age > MAX_AGE:
        return "INVALID"
    
    return "OK"

tests = [
("2", "INVALID"),
(" ", "INVALID"),
("*", "INVALID"),
("abc", "INVALID"),
("0", "INVALID"),
("123", "INVALID"),
]

for value, expected in tests:
    result = validate_age(value)
    print(f"value = {value!r} expected={expected} got={result}")
    
    if result == expected:
        print("PASS")    
    else:
        print("FAIL", value, "->", result)
   

age = input("zadaj svoj vek: ")    
print(validate_age(age))
