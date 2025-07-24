#temp

def conv_temp(temp,unit):
    if unit=="C":
        return temp*(9/5 + 32)
    elif unit == "F":
        return (temp - 32 )*5/9
    else:
        return None
    

print(conv_temp(26, "C"))
    



def is_strng_pass(password):
    if len(password)<8:
        return False
    if not any (char.isdigit() for char in password):
        return False
    if not any (char.islower()for char in password):
        return False
    if not any (char.isupper()for char in password):
        return False
    if not any (char in "! @ # $ % ^ Z * (  _ )" for char in password):
        return False
    else:
        return True
    
print(is_strng_pass("mdndodn"))
print(is_strng_pass("weD2@ewneonfoek"))




def is_palin(s):
    s=s.lower().replace(" ","")
    return s==s[::-1]

print(is_palin("dwd"))  






def ttlcost(cart):
    ttl1cost=0

    for items in cart:
        ttl1cost+=items["price"]*items["quantity"]
    return ttl1cost

cart=[
    {"name": "apple", "quantity": 7, "price": 3},
    {"name": "peach", "quantity": 4, "price": 8},
    {"name": "banana", "quantity": 8, "price": 6}
]

ttl1cost = ttlcost(cart)
print(ttl1cost)



def fac(n):
    if n==0:
        return 1
    else:
        return n* fac(n-1)

print(fac(5))


