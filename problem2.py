# priting a letter with cousmized string 
letter = ''' Dear <|Name|>, 
             You are selected in apple! 
        <|Date|> '''
print(letter.replace("<|Name|>", "tiya ").replace("<|Date|>", "26 may 2028"))
