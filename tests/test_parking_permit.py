import pytest

from src.parking_permit import is_permit_valid


class TestParkingPermit:
    # TC-P01 to TC-P07: Valid input & boundary tests
    # Note: Using 'is' instead of '==' so integer 1 does NOT falsely pass as True
    @pytest.mark.parametrize("permit_active, parked_minutes, expected", [
        (True, 0, True),       # TC-P01: BVA (lower boundary)
        (True, 1, True),       # TC-P02: BVA (just above 0)
        (True, 60, True),      # TC-P03: EP (valid duration)
        (True, 119, True),     # TC-P04: BVA (just below 120 min)
        (True, 120, True),     # TC-P05: BVA (exactly 120 min)
        (True, 121, False),    # TC-P06: BVA (just above 120 min)
        (False, 60, False),    # TC-P07: EP (inactive permit)
    ])
    def test_is_permit_valid(self, permit_active, parked_minutes, expected):
        assert is_permit_valid(permit_active, parked_minutes) is expected

    # TC-P08: Output type check
    def test_is_permit_valid_return_type(self):
        result = is_permit_valid(True, 60)
        assert type(result) is bool

    # TC-P09: ValueError for negative minutes
    def test_is_permit_valid_value_error(self):
        with pytest.raises(ValueError):
            is_permit_valid(True, -1)

    # TC-P10 to TC-P13: TypeError for invalid parameter data types
    @pytest.mark.parametrize("permit_active, parked_minutes", [
        (1, 60),            # TC-P10: EP (permit is int not bool)
        ("True", 60),       # TC-P11: EP (permit is string)
        (True, 60.0),       # TC-P12: EP (minutes is float)
        (True, False),      # TC-P13: EP (minutes is bool not int)
    ])
    def test_is_permit_valid_type_error(self, permit_active, parked_minutes):
        with pytest.raises(TypeError):
            is_permit_valid(permit_active, parked_minutes)