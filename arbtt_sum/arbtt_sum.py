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

    for D, V in byday.items():
        M = dateparser.parse(D)
        if M is not None:
            print(">" + M.strftime(dayfmt))
        else:
            print(">" + D)

        d = V.days * 24
        hours = round(V.seconds / 3600 + d, 2)
        print(f"{hours}h")


def main():
    process_arbtt_stats_text(sys.stdin.readlines())


if __name__ == "__main__":
    main()
