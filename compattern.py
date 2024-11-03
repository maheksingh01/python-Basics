def solidSquare(rows): 
  
    for i in range(1, rows): 
          
        # Print stars after spaces 
        for j in range(1, rows + 1): 
            print("*", end = "") 
  
        # Move to the next line/row 
        print() 
        
        
# def lshape(rows):
#     result_str = ""

#     # Iterate through rows from 0 to 6 using the range function
#     for row in range(1, 5):
#         # Iterate through columns from 0 to 6 using the range function
#         for column in range(1, 5):
#             # Check conditions to determine whether to place '*' or ' ' in the result string
            
#             # If conditions are met, place '*' in specific positions based on row and column values
#             if (column == 1 or (row == 6 and column != 0 and column < 6)):
#                 result_str = result_str + "*"  # Append '*' to the 'result_str'
#             else:
#                 result_str = result_str + " "  # Append space (' ') to the 'result_str'

#         result_str = result_str   # Add a newline character after each row in 'result_str'

#     # Print the final 'result_str' containing the pattern
#     print(result_str) 


rows = 5
# lshape(rows);
solidSquare(rows);
