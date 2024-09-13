def calculate_profit(cost_price, selling_price):
    """
    Функция вычисляет прибыль на основе себестоимости и цены продажи.

    :param cost_price: Себестоимость товара
    :param selling_price: Цена продажи товара
    :return: Прибыль
    """
    profit = selling_price - cost_price
    return profit


# Пример использования
cost_price = float(input("Введите себестоимость товара: "))
selling_price = float(input("Введите цену продажи товара: "))

profit = calculate_profit(cost_price, selling_price)
print(f"Прибыль: {profit:.2f}")
