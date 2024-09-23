def final_price(price, discount = 10):
    result = price - (price * discount / 100)
    print(f'цена с учётом скидки - {result}')

final_price(23000)
final_price(discount=23, price=23000)