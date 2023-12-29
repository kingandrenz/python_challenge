def your_vat():
    """ return price plus VAT """
    while True:
        price = input('please enter price :')

        if price == 'q':
            break

        try:
            vat = (15 / 100) * int(price)
            price_vat = int(price) + vat
        except ValueError:
            print('please enter a valid number')
        else:
            return int(price_vat)

print(your_vat())
