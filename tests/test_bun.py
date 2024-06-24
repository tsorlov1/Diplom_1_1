from praktikum.bun import Bun
from data import DataBun


class TestBuns:

    def test_get_name_bun(self):
        bun = Bun(DataBun.BLACK_BUN, DataBun.BLACK_BUN_PRICE)
        assert bun.get_name() == DataBun.BLACK_BUN

    def test_get_price_bun(self):
        bun = Bun(DataBun.BLACK_BUN, DataBun.BLACK_BUN_PRICE)
        assert bun.get_price() == DataBun.BLACK_BUN_PRICE
