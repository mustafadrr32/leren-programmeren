def generate_series():
    series = ["1"]
    
    while True:
        current = series[-1]
        next_num = ""
        count = 1
        
        for i in range(1, len(current)):
            if current[i] == current[i-1]:
                count += 1
            else:
                next_num += str(count) + current[i-1]
                count = 1
        
        next_num += str(count) + current[-1]
        series.append(next_num)
        
        if "33" in next_num:
            break
    
    return series

series = generate_series()

for num in series:
    print(num)