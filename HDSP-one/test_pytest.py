import pytest
from allure_commons.model2 import Attachment


def div(a, b):
    #tod0:健壮性，异常处理
    #先写测试用例 -测试驱动开发 0TDD（ Test_driven development）
    return a / b

@pytest.mark.happy
def test_div_int():
    assert div(10, 2) > 4

@pytest.mark.happy
def test_div_float():
    assert div(10, 3) == 3.333
    assert div(10.2, 2) == 5

@pytest.mark.happy
def test_div_expection():
    assert div(10, 'a')

