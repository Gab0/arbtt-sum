# About

This utility helps to sum hours captured with `arbtt`.

# Setup

Two options: 

- a) Install the module with `pip install .`
- b) Place the python script `arbtt_sum/arbtt_sum.py` on your `$PATH`.

# Usage

- a) Show daily hours: `$arbtt-stats --for-each=day | arbtt-sum`
- b) Show all hours `$arbtt-stats | arbtt-sum`

All other `arbtt-stats` filters will work, as long as `arbtt`'s `--output-format` is `text`.
Your `categorize.cfg` will be respected. This utility only sums the hours as output by `arbtt-stats`.


# TODO

- Take advantage of `csv` exporting capabilities of `arbtt-stats`.
