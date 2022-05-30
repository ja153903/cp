class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        items = sentence.split(" ")

        prices = [
            item for item in items if item.startswith("$") and self.is_float(item[1:])
        ]
        price_indices = [
            i
            for i, item in enumerate(items)
            if item.startswith("$") and self.is_float(item[1:])
        ]

        discounted_prices = [
            float(price[1:]) * (1 - discount * 0.01) for price in prices
        ]

        discounted_prices = [f"${price:.2f}" for price in discounted_prices]

        for i in price_indices:
            items[i] = discounted_prices.pop(0)

        return " ".join(items)

    def is_float(self, s: str) -> bool:
        try:
            float(s)
            return True
        except ValueError:
            return False
