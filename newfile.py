import re

menu = ['pizza','pizzas','burger','burgers','pasta','pastas']
# para = "Hi I want to order 2 pizza and 5 burgers"

def convert(para):
    order = []
    
    para = para.lower()
    text = para.split()
    for word in text:
        if word in menu:
            order.append(word)

    pattern = r'\d+\.?\d*'
    numbers = re.findall(pattern, para)
    return order,numbers
# order = []  
#order,quantity = convert(para)

# for i in order:
#     print(i)
