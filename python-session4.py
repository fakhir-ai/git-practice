list_1 = [1,"a",200,"bced"]
list_2 = [2,"ccc",332,"asds"]
#list_1.append(list_2)
list_1.extend(list_2)
print(list_1)
print(list_1[4])
for index,element in enumerate(list_1):
    print(f"index: {index}, element: {element}")
#count the number of occurences of each word
'''input_list = ["The", "THE","the","a","The","The"]
input_list_lower = [item.lower() for item in input_list]
input_set = set(input_list_lower)
result_set = [[word,input_list_lower.count(word)] for word in input_set]
print(result_set)'''
# Find the total count for each order status in a tuple 
data = '''order_id, order_amount, order_status
101, 1200, Completed
102, 1100, Pending
103, 800, Processing
104, 500, Completed
105, 600, Processing
106, 720, Completed'''
no_header_data = data.split("\n")[1:]
tuple_data = [tuple(item.split(",")) for item in no_header_data]
status_column = [status[2] for status in tuple_data]
unique_status = set(status_column)
status_count = [[count_status, status_column.count(count_status)] for count_status in unique_status]
print(status_count)
