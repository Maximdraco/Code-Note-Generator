import re

with open('Input.txt', 'r') as file_a:
    Code_Notes = file_a.readlines()
"""
Separate each line in 3 components, the
addres, the Bitx and the note and save
it in a tuple
"""
lines = [] # List to save each tuple
for line in Code_Notes:
    match = re.match(r'^\w+', line)
    if match:
        Addres = match.group(0)
    else:
        Addres = ""
    rest = line[len(Addres):]

    match = re.search(r'Bit\d\s*=', line)

    if match:
        Bit = match.group(0)
    else:
        Bit = ""
    rest = line[match.end():].lstrip()
    rest = rest.rstrip("\n")
    Tuple = (Addres, Bit, rest)
    
    lines.append(Tuple)
#--------------------------------
"""
Save each addres in a list to use later
"""
Addreses = []
for element in lines:
    if element[0] not in Addreses:
        Addreses.append(element[0])
#-------------------------------
"""
Create a string with the format of the
unpublished code notes in RACache for
each different addres
"""
addres = "z"
new_list = []
Line = ""
for element in lines:
    if element[0] != addres:
        if Line != "":
            new_list.append(Line)
        addres = element[0]
        Line = "\\r\\n"+element[1]+" "+element[2]
    else:
        Line+= "\\r\\n"+element[1]+" "+element[2]
new_list.append(Line)
#---------------------------------
"""
Write each Code note with the correct
format in another .txt ready to copy
and paste in the [Game ID]-User.txt file
"""
with open('Output.txt', 'w') as file_b:
    counter = 0
    for addres in Addreses:
        file_b.write("N0:"+Addreses[counter]+":\"[Offset] Event Flags\\r\\n"+new_list[counter]+"\"\n")
        counter += 1
print("Thanks for using this program")
