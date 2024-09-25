#Create Nested list with List Comprehension
# Output should be like this [[1,1,1],[2,4,8],[3,9,27]]

nested_list = [[num**1, num**2, num**3] for num in range(1,4)]
print(nested_list)
