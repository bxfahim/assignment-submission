mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here
# import random
'''
Recently Xiaomi Note 5 has been released. The price of this model is 300 USD which is 300 x 103.25 tk BDT. 
It has manufactured and made in China.

'''

# print(type(mobile_data))
mobile_data_list = mobile_data.get("data")
# print(len(mobile_data_list))
print(mobile_data_list)
# # price = mobile_data_list[0].values()
# print(price)
# print(type(price))
# # new_price_int = int(price)
# # print(new_price_int)
# # print(type(new_price_int))

for mobile_selling_data in mobile_data_list:
    price = mobile_selling_data.get("price")
    name = mobile_selling_data.get("name")
    made = mobile_selling_data.get("made")


    template = f'Recently {name} has been released.' \
              f'The price of this model is {price} USD which is {price} tk BDT. ' \
              f'It has manufactured and made in {made}.'
    print(template)
    print("*" * 7)














# print(type(mobile_data_list[1]))
#
# mobile_data_list[1].update({"price": 300 * 103.25 })
#
# for x in mobile_data_list.values("price", (300 * 2)):
#     print(mobile_data_list.get("price"))

# for mobile_data_dictionary in mobile_data_list:
#     # print(mobile_data_dictionary)
#     price = mobile_data_dictionary.get("price")
#     print(price)

    # bdt = int(price * 103.25)
    # print(bdt)



# for mobile in mobile_data_list:
#     text = [
#         f'Recently {mobile.get("name")} has been released.',
#         f'The price of this model is 300 USD which is {mobile.get("price")} tk BDT.',
#         f'It has manufactured and made in {mobile.get("made")}.',
#     ]
#
#     print(' '.join(text))
#
#     print(mobile_data.values('price: ')