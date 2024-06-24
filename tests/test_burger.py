import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from data import DataBun, DataIngredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_set_buns_burger(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = DataBun.BLACK_BUN
        mock_bun.get_price.return_value = DataBun.BLACK_BUN_PRICE
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, DataIngredient.INGREDIENT_NAME_HOT_SAUCE,
         DataIngredient.INGREDIENT_PRICE_HOT_SAUCE),
        (INGREDIENT_TYPE_FILLING, DataIngredient.INGREDIENT_NAME_CHILI_CUTLET,
         DataIngredient.INGREDIENT_PRICE_CHILI_CUTLET)
    ])
    def test_add_ingredient_burger(self, ingredient_type, name, price):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = name
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].get_name() == name

    def test_remove_ingredient_burger(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_burger(self):
        burger = Burger()
        mock_ingredient_one = Mock()
        mock_ingredient_two = Mock()
        burger.add_ingredient(mock_ingredient_one)
        burger.add_ingredient(mock_ingredient_two)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient_two, mock_ingredient_one]

    def test_get_price_burger(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = DataBun.BLACK_BUN_PRICE
        mock_ingredient_one = Mock()
        mock_ingredient_one.get_price.return_value = 100
        mock_ingredient_two = Mock()
        mock_ingredient_two.get_price.return_value = 100
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_one)
        burger.add_ingredient(mock_ingredient_two)
        assert burger.get_price() == 400

    def test_get_receipt_burger(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = DataBun.BLACK_BUN
        mock_bun.get_price.return_value = DataBun.BLACK_BUN_PRICE

        mock_ingredient_one = Mock()
        mock_ingredient_one.get_type.return_value = DataIngredient.INGREDIENT_TYPE_FILLING
        mock_ingredient_one.get_name.return_value = DataIngredient.INGREDIENT_NAME_CHILI_CUTLET
        mock_ingredient_one.get_price.return_value = DataIngredient.INGREDIENT_PRICE_CHILI_CUTLET

        mock_ingredient_two = Mock()
        mock_ingredient_two.get_type.return_value = DataIngredient.INGREDIENT_TYPE_SAUCE
        mock_ingredient_two.get_name.return_value = DataIngredient.INGREDIENT_NAME_HOT_SAUCE
        mock_ingredient_two.get_price.return_value = DataIngredient.INGREDIENT_PRICE_HOT_SAUCE

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_one)
        burger.add_ingredient(mock_ingredient_two)
        expected_receipt = f'(==== {DataBun.BLACK_BUN} ====)\n= filling {DataIngredient.INGREDIENT_NAME_CHILI_CUTLET} =\n= sauce {DataIngredient.INGREDIENT_NAME_HOT_SAUCE} =\n(==== {DataBun.BLACK_BUN} ====)\n\nPrice: 400'
        assert burger.get_receipt() == expected_receipt
