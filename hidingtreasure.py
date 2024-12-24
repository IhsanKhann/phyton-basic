line1 = ["a","b","c"]
line2 = ["d","e","f"]
line3 = ["g","h","i"]
map = [line1,line2,line3]
#User input: 
position = input("Position where you want to hide the treasure.") #Suppose he enter position - b3
abc = ["a","b","c"]                    #this is the column labels.
column_index = position[0].lower()     #converts the capital to small.
letter_index = abc.index(column_index) #convert the column index to int.
#now store the row_index: 
row_index = int(position[1])-1          #minus one from the row number. 
map[letter_index][row_index] = "x"
print (f"{line1} \n {line2} \n {line3}")

