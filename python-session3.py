#Create Nested list with List Comprehension
# Output should be like this [[1,1,1],[2,4,8],[3,9,27]]

nested_list = [[num**1, num**2, num**3] for num in range(1,4)]
print(nested_list)

# Output should be like this [1,1,1,2,4,8,3,9,27]
flattened_list = [item for sublist in nested_list for item in sublist ]
print(flattened_list)
#find the order status in a list
orders_list = [[101,"Closed"],[102,"Pending"],[103,"Complete"]]
orders_status = [orders[0] for orders in orders_list if orders[1] == 'Closed']
print(orders_status)