import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from data import DataBun, DataIngredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_set_buns_burger(self):
        bun = Bun(DataBun.BLACK_BUN, DataBun.BLACK_BUN_PRICE)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, DataIngredient.INGREDIENT_NAME_HOT_SAUCE,
         DataIngredient.INGREDIENT_PRICE_HOT_SAUCE),
        (INGREDIENT_TYPE_FILLING, DataIngredient.INGREDIENT_NAME_CHILI_CUTLET,
         DataIngredient.INGREDIENT_PRICE_CHILI_CUTLET)
    ])
    def test_add_ingredient_burger(self, ingredient_type, name, price):
        burger = Burger()
        ingredient = Ingredient(ingredient_type, name, price)
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0].get_name() == name

    def test_remove_ingredient_burger(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, DataIngredient.INGREDIENT_NAME_HOT_SAUCE,
                                DataIngredient.INGREDIENT_PRICE_HOT_SAUCE)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_burger(self):
        burger = Burger()
        ingredient_one = Ingredient(INGREDIENT_TYPE_SAUCE, DataIngredient.INGREDIENT_NAME_HOT_SAUCE,
                                    DataIngredient.INGREDIENT_PRICE_HOT_SAUCE)
        ingredient_two = Ingredient(INGREDIENT_TYPE_FILLING, DataIngredient.INGREDIENT_NAME_CHILI_CUTLET,
                                    DataIngredient.INGREDIENT_PRICE_CHILI_CUTLET)
        burger.add_ingredient(ingredient_one)
        burger.add_ingredient(ingredient_two)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_two, ingredient_one]

    def test_get_price_burger(self):
        burger = Burger()
        bun = Bun(DataBun.BLACK_BUN, DataBun.BLACK_BUN_PRICE)
        ingredient_one = Ingredient(INGREDIENT_TYPE_SAUCE, DataIngredient.INGREDIENT_NAME_HOT_SAUCE,
                                    DataIngredient.INGREDIENT_PRICE_HOT_SAUCE)
        ingredient_two = Ingredient(INGREDIENT_TYPE_FILLING, DataIngredient.INGREDIENT_NAME_CHILI_CUTLET,
                                    DataIngredient.INGREDIENT_PRICE_CHILI_CUTLET)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_one)
        burger.add_ingredient(ingredient_two)
        assert burger.get_price() == 400

    def test_get_receipt_burger(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = DataBun.BLACK_BUN
        mock_bun.get_price.return_value = DataBun.BLACK_BUN_PRICE

        mock_ingredient_one = Mock()
        mock_ingredient_one.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient_one.get_name.return_value = DataIngredient.INGREDIENT_NAME_CHILI_CUTLET
        mock_ingredient_one.get_price.return_value = DataIngredient.INGREDIENT_PRICE_CHILI_CUTLET

        mock_ingredient_two = Mock()
        mock_ingredient_two.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient_two.get_name.return_value = DataIngredient.INGREDIENT_NAME_HOT_SAUCE
        mock_ingredient_two.get_price.return_value = DataIngredient.INGREDIENT_PRICE_HOT_SAUCE

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_one)
        burger.add_ingredient(mock_ingredient_two)
        expected_receipt = f'(==== {DataBun.BLACK_BUN} ====)\n= filling {DataIngredient.INGREDIENT_NAME_CHILI_CUTLET} =\n= sauce {DataIngredient.INGREDIENT_NAME_HOT_SAUCE} =\n(==== {DataBun.BLACK_BUN} ====)\n\nPrice: 400'
        assert burger.get_receipt() == expected_receipt
