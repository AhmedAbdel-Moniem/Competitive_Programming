# Code wars, Your Order Please solution.
def your_order_plz(my_text):
	splits = my_text.split(" ")
	my_list =[]
	for i in range(1, 10):
		for k in splits:
			if str(i) in k:
				my_list.append(k)
	return " ".join(my_list)


a_string = "ahm6ed abde2l mon1iem mo5hamed ab4del gawa3d"
print(your_order_plz(a_string))