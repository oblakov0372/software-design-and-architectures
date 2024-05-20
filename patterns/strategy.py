from abc import ABC, abstractmethod


class ShippingCostStrategy(ABC):
    @abstractmethod
    def calculate(self, order):
        pass


class FixedCostStrategy(ShippingCostStrategy):
    def calculate(self, order):
        return 10  # фиксированная стоимость доставки


class WeightBasedStrategy(ShippingCostStrategy):
    def calculate(self, order):
        return order["weight"] * 1.5  # стоимость на основе веса


class DistanceBasedStrategy(ShippingCostStrategy):
    def calculate(self, order):
        return order["distance"] * 0.5  # стоимость на основе расстояния


class ShippingCostCalculator:
    def __init__(self, strategy: ShippingCostStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ShippingCostStrategy):
        self._strategy = strategy

    def calculate_cost(self, order):
        return self._strategy.calculate(order)


# Пример использования
order = {"weight": 10, "distance": 50}

# Используем фиксированную стоимость
calculator = ShippingCostCalculator(FixedCostStrategy())
cost = calculator.calculate_cost(order)
print("FixedCost:", cost)  # Output: FixedCost: 10

# Меняем стратегию на расчет на основе веса
calculator.set_strategy(WeightBasedStrategy())
cost = calculator.calculate_cost(order)
print("WeightBased:", cost)  # Output: WeightBased: 15.0

# Меняем стратегию на расчет на основе расстояния
calculator.set_strategy(DistanceBasedStrategy())
cost = calculator.calculate_cost(order)
print("DistanceBased:", cost)  # Output: DistanceBased: 25.0
