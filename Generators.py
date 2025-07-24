def Gen():
    yield 1
    yield 2

gen = Gen()
print(next(gen))

def gene(file_path):
    with open (file_path, 'r') as file:
        for line in file:
            yield line

file_path = 'sex.txt'
for lines in gene(file_path):
    print(lines.strip())

