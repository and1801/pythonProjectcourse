def cookie(start_price):
    result_price = start_price + (start_price*70/100)
    print (f'стоимость одной печеньки с наценкой - {result_price}')
    return result_price

def pack_price(cookie_price, cookie_count):
    result_price = cookie_price * cookie_count + 57
    return result_price

cookie_price = cookie(100)
pack = pack_price(cookie_price, 10)
print (f'стоимость печенек с наценкой - {pack}')