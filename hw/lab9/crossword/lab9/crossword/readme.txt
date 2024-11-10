Aaron Wang - Fund Comp - Lab 9 - crossword readme File


I went for the 15 points of extra credit.
-> I did this by having a counter that sees how many words were added through each iteration. If two of the iterations have the same amount or if all of the words are added, the program ends. 
I believe most of the functions are easily readable and describable except for the addWord function
-> The addWord loops through each character of the word to be added. It then looks to find a matching letter from words already on the board. When it finds a letter that matches, it checks if the spots that the word will fill and the surrounding spots are free. If it finds one it places it and changes the information in the word struct. Otherwise it moves on to the next word.