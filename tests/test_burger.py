from Diplom_1.burger import Burger
from Diplom_1.bun import Bun
from Diplom_1.ingredient import Ingredient
from unittest.mock import Mock, patch


class TestBurger:
    def setup_method(self):
        self.burger = Burger()

    def test_set_buns(self):
        mock_bun = Mock()
        mock_bun.name = "black bun"
        mock_bun.price = 100

        self.burger.set_buns(mock_bun)

        assert self.burger.bun.name == "black bun"
        assert self.burger.bun.price == 100

    def test_add_ingredient(self):
        mock_ingredient = Mock()
        mock_ingredient.type = 'Test ingredient type'
        mock_ingredient.name = 'Test ingredient name'
        mock_ingredient.price = 100
        
        self.burger.add_ingredient(mock_ingredient)

        assert len(self.burger.ingredients) > 0
        assert self.burger.ingredients[0].name == 'Test ingredient name'

    def test_remove_ingredient(self):
        mock_ingredient = Mock()
        mock_ingredient.type = 'Test ingredient type'
        mock_ingredient.name = 'Test ingredient name'
        mock_ingredient.price = 100
        
        self.burger.add_ingredient(mock_ingredient)
        self.burger.remove_ingredient(0)

        assert len(self.burger.ingredients) == 0

    def test_move_ingredient(self):
        mock_ingredient_1 = Mock()
        mock_ingredient_1.type = 'Test ingredient type'
        mock_ingredient_1.name = 'Test ingredient name'
        mock_ingredient_1.price = 100

        mock_ingredient_2 = Mock()
        mock_ingredient_2.type = 'Test move ingredient type'
        mock_ingredient_2.name = 'Test move ingredient name'
        mock_ingredient_2.price = 200

        self.burger.add_ingredient(mock_ingredient_1)
        self.burger.add_ingredient(mock_ingredient_2)

        self.burger.move_ingredient(1, 0)

        assert self.burger.ingredients[0].name == 'Test move ingredient name'

    @patch('Diplom_1.ingredient.Ingredient.get_price', return_value = 50)
    @patch('Diplom_1.bun.Bun.get_price', return_value = 100)
    def test_get_price(self, mock_bun_get_price, mock_ingredient_get_price,):
        bun = Bun("black bun", 100)
        ingredient = Ingredient("sauce", "hot sauce", 50)

        self.burger.set_buns(bun)
        self.burger.add_ingredient(ingredient)

        expected_result = 250
        actual_result = self.burger.get_price()

        assert actual_result == expected_result

    def test_get_receipt(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "sauce"
        mock_ingredient.get_name.return_value = "hot sauce"

        self.burger.set_buns(mock_bun)
        self.burger.add_ingredient(mock_ingredient)

        expected_receipt = '(==== black bun ====)\n' \
        '= sauce hot sauce =\n' \
        '(==== black bun ====)\n' \
        '\nPrice: 400'

        with patch('Diplom_1.burger.Burger.get_price', return_value = 400):
            assert self.burger.get_receipt() == expected_receipt
