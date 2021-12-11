import pytest
import datetime
from most_active_cookie import parse_csv, print_most_active_cookies, Cookies

LIMITED_COOKIES = Cookies({
    datetime.date(2018,12,9): [
        "AtY0laUfhglK3lC7",
        "SAZuXPGUrfbcn5UA",
        "5UAVanZf6UtGyKVS",
        "AtY0laUfhglK3lC7",
    ]
})

FULL_COOKIES = Cookies({
    datetime.date(2018,12,9): [
        "AtY0laUfhglK3lC7",
        "SAZuXPGUrfbcn5UA",
        "5UAVanZf6UtGyKVS",
        "AtY0laUfhglK3lC7",
    ],
    datetime.date(2018,12,8): [
        "SAZuXPGUrfbcn5UA",
        "4sMM2LxV07bPJzwf",
        "fbcn5UAVanZf6UtG",
    ],
    datetime.date(2018,12,7): [
        "4sMM2LxV07bPJzwf",
    ]
})

@pytest.mark.parametrize(
    "csv_file, date_to_check, expected_cookies",
    [
        (
            "cookie_log.csv",
            datetime.date(2018,12,9),
            LIMITED_COOKIES,
        ),
        (
            "cookie_log.csv",
            None,
            FULL_COOKIES,
        ),
    ],
)
def test_parse_csv(csv_file, date_to_check, expected_cookies):
    cookies = parse_csv(csv_file, date_to_check)
    assert len(cookies.cookies) == len(expected_cookies.cookies)
    assert cookies.cookies[datetime.date(2018,12,9)] == expected_cookies.cookies[datetime.date(2018,12,9)]

@pytest.mark.parametrize(
    "total_cookies, date, expected_most_active_cookies",
    [
        (
            FULL_COOKIES,
            datetime.date(2018,12,9),
            ["AtY0laUfhglK3lC7"],
        ),
        (
            FULL_COOKIES,
            datetime.date(2018,12,6),
            [],
        ),
        (
            FULL_COOKIES,
            datetime.date(2018,12,8),
            [
                "SAZuXPGUrfbcn5UA",
                "4sMM2LxV07bPJzwf",
                "fbcn5UAVanZf6UtG",
            ],
        ),
    ],
)
def test_most_active_cookies(total_cookies, date, expected_most_active_cookies):
    assert total_cookies.get_most_active_cookie(date) == expected_most_active_cookies