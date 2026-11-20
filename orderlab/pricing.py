"""Pricing calculation module (Level 1-2)."""

FREE_SHIPPING_THRESHOLD = 50_000
STANDARD_SHIPPING_FEE = 3_000


def subtotal(price: int, quantity: int) -> int:
    if price < 0 or quantity < 0:
        raise ValueError("단가와 수량은 음수일 수 없습니다.")
    return price * quantity

