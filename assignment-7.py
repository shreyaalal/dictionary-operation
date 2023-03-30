D={1: 100, 2: 200, 3: 300} 

#i) Display the data at the key 2.
print(D.get(2)) 

#ii) Append the data 400 using the key 4. 
D[4] = 400
print(D)

#iii) Delete the value at key 3.
D.pop(3)
print(D)