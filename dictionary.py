'''dict_data = {"car":"bmw",
             "bike":"yamaha",
             "truck":"ashok leyland"}
print(dict_data.get("bmw"))

orders_data = [(101,1000),(201,2000),(301,3000)]
orders_dict = dict(orders_data)
print(orders_dict)
orders_keys = orders_dict.keys()
print(orders_keys)
orders_values = orders_dict.values()
print(orders_values)
orders_items = orders_dict.items()
print(orders_items)'''

customer_raw_data = '''cust_id, cust_name, cust_address
1,abc,NY
2,def,NJ
3,ghi,FL
4,jkl,GE'''
cust_header = customer_raw_data.split("\n")[0].split(",")
cust_data = customer_raw_data.split("\n")[1:]

order_raw_data = '''101,10000,1,pending
102,20000,2,closed
103,30000,3,processing
104,40000,4,completed'''
order_data = order_raw_data.split("\n")

cust_dict = {item.split(",")[0] : tuple(item.split(",")[1:]) for item in cust_data}

nested_dict = {}
for key, value in cust_dict.items():
    nested_dict[key]= {
        cust_header[1] : value[0],
        cust_header[2] : value[1]
    }
print(nested_dict)

combined_data = []
for orders in order_data:
    order = orders.split(",")
    combined_data.append((order[0],order[1],order[2],order[3],nested_dict[order[2]]))
print(combined_data)
