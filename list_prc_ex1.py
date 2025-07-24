to_do_list=["go groceries", "go run", "pay the bills", "cleaning"]

# add task
to_do_list.append("schedule a meet")

# remove task when completed'

to_do_list.remove("cleaning")

# check if task is in a list
if "pay the bills" in to_do_list:
    print("dont forget to pay the bills")

print("to do list remianing")
for task in to_do_list:
    print(f"-{task}")