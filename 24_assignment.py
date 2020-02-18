search = input("Enter the word you want to search: ")
replace = input("Enter the word that you want to replace it with: ")
with open("python.txt", "r") as fh:
    content =[] 
    for line in fh.readlines():
        content.append(line.replace(search, replace))
with open("python.txt", "w") as fh:
    for line in content:
        fh.write(line)
        
    