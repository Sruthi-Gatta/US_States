import re
lines = open('usa.states.txt').read().split('\n')
double_letter = re.compile(r'.*(.)\1.*', re.IGNORECASE)
double_letter_list = []

for line in lines:
    for word in line.split(" "):
        match = double_letter.match(word)
        if match:
            double_letter_list.append(match.group())

with open('USStates_Doubleletter.txt', 'w') as f:
    f.write('List of US States with double letter sequence' + "\n")
    for item in double_letter_list:
        f.write("%s\n" % item)