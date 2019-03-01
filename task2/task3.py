input = open("input.txt", 'r')
output = open("output.txt", "w")

fl = -1
for line in input:
    print("number is", line)

point = []
st = int(line)
i = 9
while i > 1:
    if st % i == 0:
        st = st // i
        print(i)
        point.append(i)
        fl = 1
    i = i - 1
if fl == -1:
    output.write(str(fl))

print("----------------")

for i in reversed(point):
    print(i)
    output.write(str(i))

input.close()
output.close()