import json
from pathlib import Path


def load_config(config_path):
    path = Path(config_path)
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def calculate_total(values):
    return sum(values)


def get_message():
    return "Hello, world!"


def read_default_readme():
    # open() with a fixed literal, not a parameter — must not produce a false positive
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()
