import argparse
import time
import numpy as np
import json 

from src.config_loader import load_config
from src.data_loader import load_dataset
from src.processor import generate_signal
from src.metrics import (
    create_metrics,
    create_error,
    save_metrics
)
from src.logger import setup_logger
from src.utils import set_seed


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--config", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--log-file", required=True)

    args = parser.parse_args()

    logger = setup_logger(args.log_file)

    start = time.perf_counter()

    version = "unknown"

    try:

        logger.info("Job Started")

        config = load_config(args.config)

        version = config["version"]

        logger.info(
            f"Config Loaded | "
            f"Seed={config['seed']} "
            f"Window={config['window']} "
            f"Version={version}"
        )

        set_seed(config["seed"])

        df = load_dataset(args.input)

        logger.info(f"Rows Loaded : {len(df)}")

        df = generate_signal(df, config["window"])

       

        assert "rolling_mean" in df.columns
        assert "signal" in df.columns

        assert len(df) > 0

        assert df["signal"].isin([0, 1]).all()

        assert len(df["rolling_mean"]) == len(df)

        signal_rate = df["signal"].mean()

        assert 0 <= signal_rate <= 1

        latency = (time.perf_counter() - start) * 1000

        metrics = create_metrics(
            version,
            len(df),
            signal_rate,
            latency,
            config["seed"]
        )

        save_metrics(metrics, args.output)

        logger.info("Rolling Mean Computed")

        logger.info("Signals Generated")

        logger.info(f"Signal Rate : {signal_rate:.4f}")

        logger.info("Job Completed Successfully")

        print(json.dumps(metrics, indent=4))

    except Exception as e:

        logger.exception(str(e))

        metrics = create_error(version, str(e))

        save_metrics(metrics, args.output)

        print(json.dumps(metrics, indent=4))

        raise


if __name__ == "__main__":
    main()