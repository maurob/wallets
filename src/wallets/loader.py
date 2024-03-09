import yaml


def load_file(filename):
    with open(filename) as f:
        return yaml.safe_load(f)
