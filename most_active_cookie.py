import argparse
import datetime
from typing import List, Mapping, Optional
from collections import defaultdict, Counter

class Cookies:
    def __init__(
        self,
        cookies: Mapping[datetime.date, List[str]],
    ):
        self.cookies = cookies

    def get_most_active_cookie(
        self,
        date: datetime.date,
        ) -> Optional[List[str]]:
        """Get the most active cookie(s) for the given date.
        Time: O(n), n = number of cookies for a given date

        Input:
            date: YYYY-MM-DD
        
        Returns a list of cookies that are the most frequent for the date
        or None if date is not present in the table
        """
        if date not in self.cookies:
            return []
        curr_cookies = self.cookies[date]
        cookie_counter = Counter(curr_cookies)
        max_cookie_val = max(cookie_counter.values())
        max_cookies = filter(lambda x: x[1] == max_cookie_val, cookie_counter.items())
        return [key for key, _ in max_cookies]


def parse_csv(
    csv_file: str,
    date_to_check: datetime.date = None
) -> Cookies:
    """Parses csv file with an optimization option to only parse until a given date

    Input:
        csv_file: file name
        date_to_check: date to stop parsing csv (inclusive),
            None if parsing all the way through

    Returns Cookies object with cookies stored for each date
    """
    assert csv_file[-4:] == ".csv", (
        "File is not a csv file"
    )
    cookies = defaultdict(list)
    with open(csv_file) as file:
        line = file.readline() #skip headers
        line = file.readline()
        while line:
            curr_cookie, curr_datetime_str = line.strip().split(',')
            curr_date_str = curr_datetime_str.split('T')
            curr_date = datetime.date.fromisoformat(curr_date_str[0])

            if date_to_check and curr_date < date_to_check:
                break

            cookies[curr_date].append(curr_cookie)
            line = file.readline()
    
    return Cookies(cookies=cookies)

def print_most_active_cookies(
    csv_file: str,
    date: datetime.date,
) -> Optional[List[str]]:
    """Print the most active cookie(s) for the given date

    Input:
        csv_file: file name
        date: date of interest YYYY-MM-DD

    Returns the most active cookies(s) for the given date
    """

    all_cookies = parse_csv(csv_file, date)
    most_active_cookies = all_cookies.get_most_active_cookie(date)
    if most_active_cookies:
        for cookie in most_active_cookies:
            print(cookie)
    else:
        print("There were no cookies for that date. ")
    return most_active_cookies

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file")
    parser.add_argument('-d', '--date', type=datetime.date.fromisoformat, metavar='YYYY-MM-DD')
    
    args = parser.parse_args()
    csv_file = args.csv_file
    date = args.date

    print_most_active_cookies(csv_file, date)
    
if __name__ == "__main__":
    main()
