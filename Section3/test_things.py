stores = [
            {
              "items": [
                {
                  "name": "banana",
                  "price": 15.99
                },
                {
                  "name": "potatoes",
                  "price": 4.99
                }
              ],
              "name": "store1"
            },
            {
              "items": [
                {
                  "name": "apples",
                  "price": 12.99
                }
              ],
              "name": "store2"
            }
        ]


print(stores)
for store in stores:
    print('Store name {} '.format(store['name']))
    for item in store['items']:
        print(item)

