list_1 = [1,"a",200,"bced"]
list_2 = [2,"ccc",332,"asds"]
#list_1.append(list_2)
list_1.extend(list_2)
print(list_1)
print(list_1[4])
for index,element in enumerate(list_1):
    print(f"index: {index}, element: {element}")

#count the number of occurences of each word
input_list = ["The", "THE","the","a","The","The"]
input_list_lower = [item.lower() for item in input_list]
input_set = set(input_list_lower)
result_set = [[word,input_list_lower.count(word)] for word in input_set]
print(result_set)