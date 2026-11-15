
import pytest

from src.parking_fee import calculate_parking_fee

class TestParkingFee:
    # TC-F01 to TC-F10: Valid input tests
    @pytest.mark.parametrize("minutes, expected", [
        (0, 0),          # TC-F01: BVA (lower boundary)
        (2, 200),        # TC-F02: BVA (just above 0)
        (45, 200),       # TC-F03: EP (partial hour)
        (179, 600),      # TC-F04: BVA (just below 3 hr)
        (180, 600),      # TC-F05: BVA (exactly 3 hr)
        (181, 800),      # TC-F06: BVA (just above 3 hr)
        (239, 800),      # TC-F07: BVA (just below 4 hr)
        (240, 800),      # TC-F08: BVA (exactly 4 hr)
        (241, 1000),     # TC-F09: BVA (just above 4 hr)
        (2880, 9600),    # TC-F10: EP (large valid value)
    ])
    def test_calculate_parking_fee_valid(self, minutes, expected):
        assert calculate_parking_fee(minutes) == expected

    # TC-F11: Output type check
    def test_calculate_parking_fee_return_type(self):
        result = calculate_parking_fee(181)
        assert type(result) is int

    # TC-F12: Value Error
    def test_calculate_parking_fee_value_error(self):
        with pytest.raises(ValueError):
            calculate_parking_fee(-5)

    # TC-F13 to TC-F15: Type Errors
    @pytest.mark.parametrize("invalid_input", [
        False,     # TC-F13: EP (bool not int)
        180.5,     # TC-F14: EP (float)
        "180"      # TC-F15: EP (string)
    ])
    def test_calculate_parking_fee_type_error(self, invalid_input):
        with pytest.raises(TypeError):
            calculate_parking_fee(invalid_input)