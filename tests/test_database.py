from Diplom_1.database import Database


class TestDataBase:
    def setup_method(self):
        self.database = Database()

    def test_available_buns(self):
        buns = self.database.available_buns()

        assert len(buns) > 2
        assert any(bun.name == "black bun" and bun.price == 100 for bun in buns)

    def test_available_ingredients(self):
        ingredients = self.database.available_ingredients()

        assert len(ingredients) > 5
        assert any(ingredient.name == "hot sauce" and ingredient.price == 100 for ingredient in ingredients)
