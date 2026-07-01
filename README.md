# MLOps Technical Assessment – Task 0

A minimal MLOps-style batch processing pipeline built in Python that demonstrates reproducibility, observability, validation, and Docker deployment readiness.

---

## Project Objective

This project implements the requirements of the Task 0 Technical Assessment by:

- Loading configuration from a YAML file
- Reading OHLCV market data from a CSV file
- Computing a rolling mean on the `close` column
- Generating binary trading signals
- Producing structured metrics in JSON format
- Creating detailed execution logs
- Supporting Docker-based execution

---

## Project Structure

```
mltask/
│
├── run.py
├── config.yaml
├── data.csv
├── requirements.txt
├── Dockerfile
├── README.md
├── metrics.json
├── run.log
│
└── src/
    ├── config_loader.py
    ├── data_loader.py
    ├── processor.py
    ├── metrics.py
    ├── logger.py
    └── utils.py
```

---

## Features

- YAML configuration loading
- Configuration validation
- Dataset validation
- Rolling mean calculation
- Binary signal generation
- Deterministic execution using a fixed random seed
- Structured metrics generation
- Detailed logging
- Dockerized execution
- Proper exception handling

---

## Configuration

Example `config.yaml`

```yaml
seed: 42
window: 5
version: "v1"
```

---

## Signal Logic

Rolling mean is computed using the configured window size.

```
signal = 1  if close > rolling_mean
signal = 0  otherwise
```

For the first `window - 1` rows, the rolling mean is unavailable (`NaN`), and the signal is set to `0` to maintain consistency.

---

## Validation

The application validates:

### Configuration

- Required fields exist
    - seed
    - window
    - version
- Window is a positive integer

### Dataset

- Input file exists
- CSV format is valid
- Dataset is not empty
- Required column `close` exists

### Consistency Checks

- rolling_mean column created
- signal column created
- signal contains only 0 or 1
- Output row count matches input
- Signal rate is within [0,1]

---

## Output

### metrics.json

Example:

```json
{
    "version": "v1",
    "rows_processed": 10000,
    "metric": "signal_rate",
    "value": 0.4989,
    "latency_ms": 19,
    "seed": 42,
    "status": "success"
}
```

---

### run.log

Contains:

- Job start
- Configuration details
- Dataset information
- Processing steps
- Metrics summary
- Job completion
- Exception details (if any)

---

# Local Execution

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run

```bash
python run.py \
--input data.csv \
--config config.yaml \
--output metrics.json \
--log-file run.log
```

Windows PowerShell:

```powershell
python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log
```

---

# Docker

## Build

```bash
docker build -t mltask .
```

## Run

```bash
docker run --rm mltask
```

Expected output:

```json
{
    "version": "v1",
    "rows_processed": 10000,
    "metric": "signal_rate",
    "value": 0.4989,
    "latency_ms": 19,
    "seed": 42,
    "status": "success"
}
```

---

## Dependencies

- Python 3.9
- pandas
- numpy
- PyYAML

Install using:

```bash
pip install -r requirements.txt
```

---

## Reproducibility

The pipeline ensures deterministic execution by:

- Loading configuration from YAML
- Using a fixed random seed (`seed = 42`)
- Applying consistent rolling mean logic
- Producing reproducible metrics

---

## Observability

Logging includes:

- Job start timestamp
- Configuration details
- Number of rows processed
- Rolling mean computation
- Signal generation
- Metrics summary
- Job completion status
- Error information

---

## Error Handling

The application gracefully handles:

- Missing input file
- Empty CSV
- Invalid CSV format
- Missing required columns
- Invalid YAML configuration
- Missing configuration fields

In case of failure, an error `metrics.json` is still generated.

Example:

```json
{
    "version": "v1",
    "status": "error",
    "error_message": "Input file not found."
}
```

---

## Technologies Used

- Python 3.9
- Pandas
- NumPy
- PyYAML
- Docker
- Python Logging

---

## Author

**Julme Ashwitha**

MLOps Technical Assessment Submission