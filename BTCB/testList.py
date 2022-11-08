print("EXP 1 without index:") 
array = ['spam', 1, ['Brie', 'Roquefort' , 'Pol le Veq' ], [1, 2, 3]]
for item in array:
    print(item)
    
print("\nEXP 2 with index:")    
for index,item in enumerate(array):
    print(index,item)
print("\nEXP 3 with index:")
for i in range(len(array)):
    array[i] = array[i] * 2