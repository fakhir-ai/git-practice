order_amount = [100,200,50,500,400,1200,800,750]
order_amount_with_gst = []

for order_item in order_amount:
    order_amount_with_gst.append(order_item + order_item * 0.18)
print(f"Order Amount is : {order_amount}")
print(f"Order Amount with GST is : {order_amount_with_gst}")

order_gst_short = [oitem+oitem*0.18 for oitem in order_amount]
print(f"Order Amount with GST List Comprehension : {order_gst_short}")
