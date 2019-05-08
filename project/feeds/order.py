
class OrderObject(object):

    def __init__(self, items=None):

        if not items:
            items = {}

        self.items = items

    def __iter__(self):
        for item in self.items:
            item.item_name = item.product.name
            item.total_price = item.item_price * item.item_count
            yield item

    def __len__(self):
        return sum(item.item_count for item in self.items)

    def get_total_price(self):
        return sum(item.item_price * item.item_count for item in self.items)





