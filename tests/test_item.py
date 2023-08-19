"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
def test_item():
    item = Item("Планшет", 10000, 3)
    assert item.name == "Планшет"
    assert item.price == 10000
    assert item.quantity == 3
def test_calculate_total_price():
    item = Item("Планшет", 10000, 3)
    assert item.calculate_total_price() == 30000
def test_apply_discount():
    item = Item("Планшет", 10000, 2)
    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 5000