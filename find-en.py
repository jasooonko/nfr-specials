menu = open("resources/menu-list.txt", "r").readlines()
input = open("input.txt", "r").readlines()

for search in input:
    search = search.strip()
    found = False
    for line in menu:
        line = line.strip()

        if search and search in line:
            print(line)
            found = True
    if not found: 
        print(search)
