def my_discount():
    """ Return price after discount."""
    price = int(input('Please enter price: '))
    discount = int(input('Enter discount %: '))

    discount = (discount / 100) * price
    price_aftr_dis = price - discount

    return f"price after discount is: {price_aftr_dis}"

print(my_discount())
