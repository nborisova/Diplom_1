from Diplom_1.bun import Bun
import pytest


class TestBun:
    def setup_method(self):
        self.name = 'Test name'
        self.bun = Bun(self.name, 10.5)

    def test_get_name(self):
        assert self.bun.get_name() == self.name 

    @pytest.mark.parametrize('price', [10.5, 100, 0.01])
    def test_get_price(self, price):
        bun = Bun('Test name', price)
        assert bun.get_price() == price
