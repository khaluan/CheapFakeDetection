with open('../Output/url.txt', 'r', encoding='utf8') as file:
    append_data = file.readlines()[::-1]

with open('../Output/url_full.txt', 'r', encoding='utf8') as file:
    data = file.readlines()[::-1]
print(len(data))
j = 0
for i in range(len(data)-1):
    if data[i] == data[i+1]:
        if i == 76:
            continue
        data[i] = append_data[j]
        j += 1

data = data[::-1]
print(len(data))
with open('../Output/url_merged.txt', 'w+', encoding='utf8') as file:
    for d in data:
        file.write(d)
        if d[-1] != '\n':
            print('bingo')
            file.write('\n')
    

