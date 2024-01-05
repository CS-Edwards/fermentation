import numpy as np
import pytest
from fermentation.metrics import calc_extract


def test_calc_extract():
    """
    Test calc extract
    """
    expected_value = 5
    calc_value = calc_extract(25)
    np.testing.assert_equal(calc_value, expected_value)


@pytest.mark.parametrize(
    "input_value, expected_value",
    [(25, 5), (5, None)],
)
def test_calc_extract_parameterized(input_value, expected_value):
    """Test that rescale works correctly for multiple cases."""
    calc_value = calc_extract(input_value)
    np.testing.assert_equal(calc_value, expected_value)
