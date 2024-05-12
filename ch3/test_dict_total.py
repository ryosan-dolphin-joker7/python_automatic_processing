dummy_data = [
        ["伊藤", 300], ["伊藤", 600], ["伊藤", 200], 
        ["田中", 300], ["田中", 200]]
total = {"伊藤":0, "田中":0}
for name, value in dummy_data: total[name] += value
print(total)

