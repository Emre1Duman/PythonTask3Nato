#Message = ('If, you can read?')
#UserInput = input('Enter Message: ')
#test

d =  {
        'A': 'Alpha',  'B': 'Bravo',   'C': 'Charlie',
        'D': 'Delta',  'E': 'Echo',    'F': 'Foxtrot',
        'G': 'Golf',   'H': 'Hotel',   'I': 'India',
        'J': 'Juliett','K': 'Kilo',    'L': 'Lima',
        'M': 'Mike',   'N': 'November','O': 'Oscar',
        'P': 'Papa',   'Q': 'Quebec',  'R': 'Romeo',
        'S': 'Sierra', 'T': 'Tango',   'U': 'Uniform',
        'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
        'Y': 'Yankee', 'Z': 'Zulu'}

    
UserInput = input('Enter Message: ')
for letter in UserInput:
        print(d.get(letter.upper()), end=' ')

#print(' '.join(d.get(letter.upper(), letter) for letter in UserInput))

#file = open("Task3.txt", "r")

#print("First line: ")
 

  #  file.close()
