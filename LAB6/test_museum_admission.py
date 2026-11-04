
import pytest
from museum_admission import ticket_price, group_discount, gallery_entry


#test cases for ticket price

def test_adult_weekday():
    assert ticket_price("adult", 30, "tuesday", False) == 300


def test_student_ticket():
    assert ticket_price("student", 20, "tuesday", False) == 150


def test_child_ticket():
    assert ticket_price("child", 10, "tuesday", False) == 100


def test_senior_ticket():
    assert ticket_price("senior", 65, "tuesday", False) == 200


def test_unknown_category():
    with pytest.raises(ValueError, match="unknown category"):
        ticket_price("invalid", 30, "tuesday", False)


def test_negative_age():
    with pytest.raises(ValueError, match="invalid age"):
        ticket_price("adult", -1, "tuesday", False)


def test_free_entry_below_five():
    assert ticket_price("adult", 4, "tuesday", False) == 0


def test_age_exactly_five():
    assert ticket_price("adult", 5, "tuesday", False) == 300


def test_monday_discount():
    assert ticket_price("adult", 30, "monday", False) == 150


def test_saturday_extra_charge():
    assert ticket_price("adult", 30, "saturday", False) == 350


def test_sunday_extra_charge():
    assert ticket_price("adult", 30, "sunday", False) == 350


def test_student_guided_tour():
    assert ticket_price("student", 20, "tuesday", True) == 200


def test_adult_guided_tour():
    assert ticket_price("adult", 30, "tuesday", True) == 400


def test_guided_tour_with_monday_discount():
    assert ticket_price("adult", 30, "monday", True) == 250


# ==========================================
# TEST CASES FOR GROUP_DISCOUNT()
# ==========================================

def test_invalid_group_size():
    with pytest.raises(ValueError, match="invalid group size"):
        group_discount(0, False)


def test_negative_group_size():
    with pytest.raises(ValueError, match="invalid group size"):
        group_discount(-5, True)


def test_school_group_twenty_or_more():
    assert group_discount(20, True) == 40


def test_school_group_above_twenty():
    assert group_discount(25, True) == 40


def test_school_group_below_twenty():
    assert group_discount(19, True) == 25


def test_non_school_group_fifteen():
    assert group_discount(15, False) == 20


def test_non_school_group_above_fifteen():
    assert group_discount(20, False) == 20


def test_non_school_group_eight():
    assert group_discount(8, False) == 10


def test_non_school_group_between_eight_and_fifteen():
    assert group_discount(10, False) == 10


def test_non_school_group_below_eight():
    assert group_discount(7, False) == 0


def test_single_person_group():
    assert group_discount(1, False) == 0


# ==========================================
# TEST CASES FOR GALLERY_ENTRY()
# ==========================================

def test_gallery_at_full_capacity():
    assert gallery_entry(100, 100, False) == "wait"


def test_gallery_above_capacity():
    assert gallery_entry(110, 100, False) == "wait"


def test_gallery_near_capacity_without_timed_slot():
    assert gallery_entry(90, 100, False) == "queue"


def test_gallery_near_capacity_with_timed_slot():
    assert gallery_entry(90, 100, True) == "enter"


def test_gallery_below_ninety_percent_capacity():
    assert gallery_entry(80, 100, False) == "enter"


def test_gallery_with_timed_slot_below_capacity():
    assert gallery_entry(50, 100, True) == "enter"
