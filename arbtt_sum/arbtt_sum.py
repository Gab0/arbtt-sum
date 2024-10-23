#!/bin/python
from typing import Dict
import re
import sys
import datetime

import dateparser

dayfmt = "%Y-%m-%d"
total_kw = "TOTAL"


def f_elapsed_time(segment):
    return re.findall(r"(\d+h)?(\d+m)?(\d+s)?", segment)


def f_identifier(segment):
    K = re.findall(r"\(Day ([^\)]+)\)", segment)
    if K:
        return dateparser.parse(K[0])


def read_time(m) -> datetime.timedelta:
    h, m, s = m
    cates = {
        "hours": h,
        "minutes": m,
        "seconds": s
    }

    for identifier, v in cates.items():
        v = v.strip("hms")
        v = float(v) if v else 0
        cates[identifier] = v

    return datetime.timedelta(**cates)


def manage_categorized_counter(d, k, v):
    if k not in d.keys():
        d[k] = datetime.timedelta(seconds=0)
    d[k] += v


def process_arbtt_stats_text(lines):
    byday: Dict[str, datetime.timedelta] = {}
    current_id = None

    for line in lines:
        ID = f_identifier(line)
        if ID:
            current_id = ID
        for match in f_elapsed_time(line):
            if any(match):
                K = read_time(match)
                manage_categorized_counter(byday, total_kw, K)
                if current_id is not None:
                    manage_categorized_counter(byday, str(current_id), K)
    return byday


def show_byday_stats(byday):
    for D, V in byday.items():
        M = dateparser.parse(D)
        if M is not None:
            print(">" + M.strftime(dayfmt))
        else:
            print(">" + D)

        hours = datetime2hours(V)
        print(float_hours_to_human(hours))


def datetime2hours(dt):
    return round(dt.total_seconds() / 3600, 2)


def float_hours_to_human(hours: float) -> str:
    # Remove the 'h' and convert the value to float

    # Extract the whole hours and remaining minutes
    h = int(hours)
    m = int((hours - h) * 60)

    return f"{h}h{m:02d}m"


def main():
    byday = process_arbtt_stats_text(sys.stdin.readlines())
    if sys.argv[-1] == "-u":
        print(float_hours_to_human(datetime2hours(byday["TOTAL"])))
    else:
        show_byday_stats(byday)


if __name__ == "__main__":
    main()
