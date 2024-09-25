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

#Unpacking List
order_list = [101,"2023-09-01",'1111',"CLOSED"]
order_id, order_date, customer_id, order_status = order_list
print(order_status)
#Unpacking Tuple
order_tuple = (101,"2024-09-01",'1111',"CLOSED")
order_id, order_date, customer_id, order_status = order_tuple
print(order_date)