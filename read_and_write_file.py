f_input = open('input.txt', 'r', encoding='utf8')
members = []
for temp_man in f_input:
    members.append(list(temp_man.split()))
f_input.close()
members.sort()
for man in members:
    man.pop(2)
f_output = open('output.txt', 'w', encoding='utf8')
for line in members:
    f_output.write((' '.join(map(str, line))) + '\n')
f_output.close()
