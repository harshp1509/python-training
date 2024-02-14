def generate_pattern(a):
    pattern = []
    for i in range(1, a + 1):
        row = []
        for j in range(1, i + 1):
            row.append(j)
        row += [0] * (a - i)
        pattern.append(row)
    return pattern


output = generate_pattern(3)

for row in output:
    print(row)
