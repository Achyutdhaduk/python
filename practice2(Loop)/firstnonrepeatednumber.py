input_str = 'teetrabcd'

for char in input_str:
    if input_str.count(char) == 1:
        print("First non-repeat char::",char)
        break
        