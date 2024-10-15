def print_star_pattern() :
    pattern = ""
    for row in range(9):
        for column in range(15):
            if(row == 0 and column == 0) or (row == 1 and column == 0) or (row == 2 and column == 0) or (row == 3 and column == 0) or (row == 5 and column == 14) or (row == 6 and column ==14) or (row == 7 and column == 14) or (row == 8 and column == 14) or (row == 4) or (column >=5 and column <=9 ):
                pattern += "* "
            else: 
                pattern += ' '
        pattern += '\n'
    print (pattern)
    
    
print_star_pattern()