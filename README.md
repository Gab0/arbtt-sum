# About

This utility helps to sum hours captured with `arbtt`.

# Usage

- Place on your `$PATH`.

- a) Show daily hours: `$arbtt-stats --for-each=day | arbtt_sum`

- b) Show all hours `$arbtt-stats | arbtt_sum`

All other `arbtt-stats` filters will work, as long as `arbtt`'s `--output-format` is `text`.


# TODO

- Take advantage of `csv` exporting capabilities of `arbtt`.
