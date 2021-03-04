
lines = open('usa.states.txt').read().split('\n')
alphabet_sort = sorted(lines, key=lambda x: x[0], reverse=False)
alphabet_reverse = sorted(lines, key=lambda x: x[0], reverse=True)

header1 = "US States in Alphabetical Order :"
header2 = "US States in Reverse Alphabetical Order :"
header3 = "Number of Letters in each state :"
len_states = []
with open('USStates_order.txt', 'w') as f:
    f.write(header1 + "\n")
    for item in alphabet_sort:
        f.write("%s\n" % item)
    f.write("\n")
    f.write(header3 + "\n")
    for item in lines:
        len_states = item + " " + str(len(item))
        f.write("%s\n" % len_states)
    f.write("\n")
    f.write(header2 + "\n")
    for item in alphabet_reverse:
        f.write("%s\n" % item)
