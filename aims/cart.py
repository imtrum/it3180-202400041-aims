MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self, discount = 100):
        if(discount > 100):
            raise ValueError("Discount must be smaller than 100")
        self.items = []
        self.discount = discount


    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print(f"Đã thêm đĩa '{dvd.title}' vào giỏ hàng")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
        return sum(item.cost for item in self.items) * self.discount / 100;


    def print_cart(self): #"Nếu giỏ hàng trống thì nên in 'The cart is empty'" 

        if(self.items.__len__ == 0): 
            print(f"The cart is empty")
            return
        print(f"Total cost: {self.total_cost():.2f} $")

    def sort_by_title(self):
        self.items.sort(key=lambda dvd: dvd.title.lower())

    def sort_by_cost(self):
        self.items.sort(key=lambda dvd: dvd.cost)