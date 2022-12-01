with open("elfs.txt", "r") as f: # Open the file
    data = f.read().split("\n\n") ## split on double newlines
    data = [[int(item) for item in pack.splitlines()] for pack in data] ## split on newlines and convert to int
    data = [sum(pack) for pack in data] ## sum the lists
    data = sorted(data) ## sort the list

print( "\nHow many total Calories is that Elf carrying ? " + str(data[-1]) + " Calories \n")
print( "\nHow many Calories are those Elves carrying in total ? " + str(sum(data[-3:])) + " Calories \n")