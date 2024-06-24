import pytest
from praktikum.ingredient import Ingredient
from data import DataIngredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, DataIngredient.INGREDIENT_NAME_HOT_SAUCE,
         DataIngredient.INGREDIENT_PRICE_HOT_SAUCE),
        (INGREDIENT_TYPE_FILLING, DataIngredient.INGREDIENT_NAME_CHILI_CUTLET,
         DataIngredient.INGREDIENT_PRICE_CHILI_CUTLET)
    ])
    def test_get_price_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, DataIngredient.INGREDIENT_NAME_HOT_SAUCE,
         DataIngredient.INGREDIENT_PRICE_HOT_SAUCE),
        (INGREDIENT_TYPE_FILLING, DataIngredient.INGREDIENT_NAME_CHILI_CUTLET,
         DataIngredient.INGREDIENT_PRICE_CHILI_CUTLET)
    ])
    def test_get_name_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, DataIngredient.INGREDIENT_NAME_HOT_SAUCE,
         DataIngredient.INGREDIENT_PRICE_HOT_SAUCE),
        (INGREDIENT_TYPE_FILLING, DataIngredient.INGREDIENT_NAME_CHILI_CUTLET,
         DataIngredient.INGREDIENT_PRICE_CHILI_CUTLET)
    ])
    def test_get_type_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
