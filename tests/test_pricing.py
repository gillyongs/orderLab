"""Tests for pricing module."""

import pytest

from orderlab.pricing import shipping_fee, subtotal


# ----------------------------------------------------
# 방법 1: 요구사항 ID별 개별 test_* 함수 변환
# ----------------------------------------------------
def test_t1_subtotal_normal():
    """T1: 10,000 원 × 2개 -> 20,000 원 반환 (정상)."""
    assert subtotal(10_000, 2) == 20_000


def test_t2_subtotal_zero_price():
    """T2: 0 원 × 3개 -> 0 원 반환 (경계)."""
    assert subtotal(0, 3) == 0


def test_t3_subtotal_negative_price():
    """T3: -100 원 × 2개 -> ValueError 발생 (예외)."""
    with pytest.raises(ValueError):
        subtotal(-100, 2)


def test_t4_shipping_fee_free():
    """T4: 50,000 원 × 1개 -> 무료 배송 기준 충족 (배송비 0원) (경계)."""
    amount = subtotal(50_000, 1)
    assert shipping_fee(amount) == 0


def test_t5_shipping_fee_standard():
    """T5: 49,999 원 × 1개 -> 배송비 3,000 원 추가 (경계)."""
    amount = subtotal(49_999, 1)
    assert shipping_fee(amount) == 3_000


# ----------------------------------------------------
# 방법 2: @pytest.mark.parametrize 를 사용한 표 형태 변환
# ----------------------------------------------------
@pytest.mark.parametrize(
    "price, quantity, expected",
    [
        (10_000, 2, 20_000),  # T1: 정상
        (0, 3, 0),  # T2: 경계
    ],
)
def test_subtotal_parametrized(price, quantity, expected):
    assert subtotal(price, quantity) == expected


@pytest.mark.parametrize(
    "amount, expected_fee",
    [
        (50_000, 0),  # T4: 경계 (무료 배송)
        (49_999, 3_000),  # T5: 경계 (유료 배송)
    ],
)
def test_shipping_fee_parametrized(amount, expected_fee):
    assert shipping_fee(amount) == expected_fee
