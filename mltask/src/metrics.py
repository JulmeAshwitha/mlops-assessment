import json


def create_metrics(version,
                   rows,
                   signal_rate,
                   latency,
                   seed):

    return {
        "version": version,
        "rows_processed": rows,
        "metric": "signal_rate",
        "value": float(round(signal_rate, 4)),
        "latency_ms": int(latency),
        "seed": seed,
        "status": "success"
    }


def create_error(version, message):

    return {
        "version": version,
        "status": "error",
        "error_message": message
    }


def save_metrics(metrics, output_file):
    with open(output_file, "w") as f:
        json.dump(metrics, f, indent=4)