import uuid
import time


class Good:
    def __init__(self, id: uuid, name, price: int):
        self.id = id
        self.name = name
        self.price = price

class Order:
    def __init__(self, order_id: uuid, order_date, client_id, goods: list, price = 0):
        self.order_id = order_id
        self.order_date = order_date
        self.client_id = client_id
        self.goods = goods
        self.price = price

        for good in goods:
            self.price += good.price

class OrderRepository:
    def __init__(self):
        self.orders = []

    def add(self, order: Order):
        self.orders.append(order)

    def get(self, order_id: uuid):
        for item in self.orders:
            if item.order_id == order_id:
                return item

    def list(self, n_latest:int = None):
        if n_latest is None:
            return self.orders
        else:
            return self.orders[-n_latest:]

    def delete(self, order_id: uuid):
        self.orders.remove(self.get(order_id))


f1 = Good(uuid.uuid4(), "Ronaldo", 1000)
f2 = Good(uuid.uuid4(), "Messi", 1500)
f3 = Good(uuid.uuid4(), "Dzuba", 100)
f4 = Good(uuid.uuid4(), "Cristmas_Tree", 200)

list1 = [f1, f2]
list2 = [f3, f4]

order1 = Order(uuid.uuid4(), time.time(), 'Barcelona', list1)
order2_id = uuid.uuid4()
order2 = Order(order2_id, time.time(), 'Bate', list2)

order_repository = OrderRepository()

order_repository.add(order1)
order_repository.add(order2)

assert order_repository.get(order2_id) == order2

assert order_repository.list() == [order1, order2]
assert order_repository.list(1) == [order2]

order_repository.delete(order2_id)
assert order_repository.list() == [order1]
