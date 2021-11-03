
from setuptools import setup, find_packages


setup(
    name="arbtt-sum",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "arbtt-sum=arbtt_sum.arbtt_sum:main"
        ]
    }
)
