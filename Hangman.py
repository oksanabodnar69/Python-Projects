# This is a word game
from random import choice
from collections import Counter


def selectWord(fname):
    words = open(fname).readlines()
    myword = choice(words)
    myword = str(myword).strip('  \n')
    myword = myword.lower()
    return myword


def LetterFrequency(text,size):
    counts = Counter(c for c in text if  c.strip("\n")).most_common(1)[0]
    percentege = '{0:.2f}'.format( 100*(counts[1]/ float(size)))
    print (f'{counts[0].lower()}  -  appears {counts[1]} ({percentege} %) times in the word.)')
    return str(counts[0])


def RemoveLetter(letter,text):
    return text.replace(letter,"")


def Main():
  print("Let's play the game\n")
  #select file to open
  while True:
      try:
         fname = input('Enter the file name -> ')
         break
      except:
         print('This file does not exists. Please try again!')
         continue
  # define the word
  print("Would you like to write the word or choose random from file? Please put W-write, R-random")
  variant=input(">")
  if variant.lower()=="r":
    word = selectWord(fname)
    print(word)
  else: word=input("Please enter the word: ").strip(" ")
  #define varaible
  word_list = list(word)
  blanks = "_"*len(word)
  blanks_list = list(blanks)
  new_blanks_list = list(blanks)
  temp=0
  text = open(fname).read()
  size=len(text)
  print(blanks_list)

  #suggest most resent letter in text
  while word_list != new_blanks_list:
     guess = LetterFrequency(text,size)
     i = 0
     while i < len(word):
        if guess == word[i]:
           new_blanks_list[i] = word_list[i]
        i = i+1
     temp+=1
     print(new_blanks_list)
     if word_list == new_blanks_list:
        print ("\nYOU WON!")
        print(f'You made {temp} temps to guess the word')
        quit()
     text=RemoveLetter(guess,text)

Main()
