import yaml

REQUIRED_FIELDS = ["seed", "window", "version"]


def load_config(path):
    try:
        with open(path, "r") as f:
            config = yaml.safe_load(f)

        if not isinstance(config, dict):
            raise ValueError("Config should be a dictionary.")

        for field in REQUIRED_FIELDS:
            if field not in config:
                raise ValueError(f"Missing config field: {field}")

        if not isinstance(config["window"], int):
            raise ValueError("window must be an integer.")

        if config["window"] <= 0:
            raise ValueError("window must be greater than zero.")

        return config

    except yaml.YAMLError:
        raise ValueError("Invalid YAML configuration.")