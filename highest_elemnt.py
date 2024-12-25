#print the highest score.
score = [10,20,30,40,50]
highest_element = score[0]

for high_score in score:
    if(high_score > highest_element):
        highest_element = high_score
        
print ("The highest element is:" , highest_element)
        
    