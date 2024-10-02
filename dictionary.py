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
cust_header = customer_raw_data.split("\n")[0]
cust_data = customer_raw_data.split("\n")[1:]

cust_dict = {}
for item in cust_data:
    cust_dict[item.split(",")[0]] = tuple(item.split(",")[1:])
print(cust_dict['1'])