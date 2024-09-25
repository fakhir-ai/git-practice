order_amount = [100,200,50,500,400,1200,800,750]
order_amount_with_gst = []
#List Calculation
for order_item in order_amount:
    order_amount_with_gst.append(order_item + order_item * 0.18)
print(f"Order Amount : {order_amount}")
print(f"Order Amount GST : {order_amount_with_gst}")
#List Comprehension
order_gst_short = [oitem+oitem*0.18 for oitem in order_amount]
print(f"Order Amount GST List Comprehension : {order_gst_short}")
#Tuple Calculation
tuple_amount = ((100,10),(200,12),(300,20),(500,18))
tuple_gst = []
for t_item in tuple_amount:
    tuple_gst.append(int(t_item[0]+t_item[0]*(t_item[1]/100)))
print(f"Tuple Amount : {tuple_amount}")
print(f"Tuple Amount GST : {tuple_gst}")
#Tuple Comprehension
list_gst =[int(t_item[0]+t_item[0]*(t_item[1]/100)) for t_item in tuple_amount]
print(f"Tuple Amount GST Comprehension : {list_gst}")
#Tuple List Comprehension
tuple_gst = [(t_item[0],t_item[1],int(t_item[0]+t_item[0]*(t_item[1]/100))) for t_item in tuple_amount]
print(f"Tuple GST List Comprehension : {tuple_gst}")