order_raw_data = '''101,10000,1,pending
102,20000,2,closed
103,30000,3,processing
104,40000,4,completed
105,40000,5,completed
106,40000,6,completed
107,40000,7,error'''

order_data = order_raw_data.split("\n")
order_list = [item.split(",")[3] for item in order_data]
print(f"Full order status : {order_list}")
unique_order_list = set(order_list)
print(f"Unique order status : {unique_order_list}")
valid_status = {'closed', 'completed', 'pending', 'processing'} 
invalid_status = unique_order_list - valid_status
print(f"Invalid order status : {invalid_status}")