# Code-Note-Generator
A program for Retroachievement Code Notes

Oriented to create Code Notes for Bitflags in offset addres

To use this program simply have in the same folder of the .py
file a file called "Input.txt" with the code notes you want
in the next format:

Addres Bitx = Note

"Addres" is the memory addres in hexadecimal starting with 0x

In "Bitx", the "x" is any number beetween 0 and 7

And "Note" is line of text, it have to be a single line, it
does't work well with accents or another simbols so try to 
only use ASCII characters, ideally only numbers and letters.

The program will put together all lines than share addres
and adding the necesary format to just copy and paste in 
the [Game ID]-User.txt file in RACache where you want to
place the Code notes as explained here https://github.com/RetroAchievements/docs/wiki/WIP---Dev-Tips---Code-Notes-En-Masse

The Code notes will be in a file called "Output.txt" in the
same folder, the program is very simple so feel free to edit
whathever you want to adjust it to your needs.
