# Digital Twin–Based Security Analytics for the Internet of Things (IoT)

This capstone project explores how a **Digital Twin** approach can support **security analytics for IoT systems** by modeling device behavior and using machine learning to detect suspicious or abnormal activity across multiple IoT device types.

The repository includes a training/evaluation notebook, IoT datasets, trained model artifacts, API scripts for inference, and supporting architecture/flow/sequence diagrams.

---

## What this project does

- Models IoT device behavior using a Digital Twin concept (virtual representation of device state/behavior)
- Uses ML models to learn patterns from IoT telemetry datasets
- Supports security analytics use cases such as:
  - anomaly detection / suspicious behavior identification
  - device behavior classification (depending on model setup)

---

## Contents of this repository

- **Notebook**
  - `IOT.ipynb` — data preparation, model training, testing, and evaluation

- **Datasets (CSV)**
  - `Train_Test_IoT_Fridge.csv`
  - `Train_Test_IoT_Thermostat.csv`
  - `Train_Test_IoT_Motion_Light.csv`
  - `Train_Test_IoT_Weather.csv`
  - `df.csv` (combined/processed dataset export)

- **Model Artifacts**
  - `fridgetype.pkl`
  - `thermostattype.pkl`
  - `weathertype.pkl`

- **API / Inference Scripts**
  - `api.py`
  - `api2.py`

- **Design Diagrams**
  - `architecture diagram.*`
  - `flowchart diagram.*`
  - `Seqence diagram.*` / `seqence diagram.*`

- **License**
  - MIT (`LICENSE`)

---

## Tech Stack (typical)

Python, Jupyter Notebook, Pandas, NumPy, Scikit-learn, and serialized models (`.pkl`) for inference.

---

## Author

Pranathi Gogada
