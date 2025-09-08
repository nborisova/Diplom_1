from Diplom_1.ingredient import Ingredient
import pytest


class TestIngredient:
    def setup_method(self):
        self.type = 'Test ingredient type'
        self.name = 'Test ingredient name'
        self.ingredient = Ingredient(self.type, self.name, 10.5)

    def test_get_name(self):
        assert self.ingredient.get_name() == self.name 

    @pytest.mark.parametrize('price', [10.5, 100, 0.01])
    def test_get_price(self, price):
        ingredient = Ingredient('Test ingredient type', 'Test ingredient name', price)
        assert ingredient.get_price() == price

    def test_get_type(self):
        assert self.ingredient.get_type() == self.type 