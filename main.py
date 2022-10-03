import pandas as pd
#TODO Create a morse code lookup table.
#TODO Read the morse code lookup table into dict format.
lookup = pd.read_csv('morse_code_lookup.csv', index_col=0).to_dict()

#TODO Get input string
text = input('Enter a string: ').upper()

#TODO Get the morse code of each character in the string.
#TODO Handle KeyError exception when character not in lookup table.
morse = ''
for n in range(len(text)):
    if text[n] == ' ':
        code = text[n]
    else:
        try:
            code = lookup['morse_code'][text[n]]
        except KeyError:
            code = '~'
    morse += code
    morse += ' '
#TODO Print out the result.
print(morse)

