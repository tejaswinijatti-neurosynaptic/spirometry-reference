# Indian Spirometry Reference Calculator

This folder contains Python code and documentation for calculating spirometry reference values for the **Indian population**, using weighted equations derived from multiple regional studies across India.

---

## 📄 Overview

* **Regions Covered**: North, South, East, West, Kashmir, and Northeast India
* **Parameters Predicted**: FVC, FEV1, FEV1/FVC%, PEFR, FEF25–75, FEF50, FEF75
* **Methodology**: Weighted mean based on participant count per region
* **Model Types**: Linear, quadratic, and exponential regression models

---

## 🚀 Getting Started

### 1. Requirements

Install required Python libraries:

```bash
pip install -r ../requirements.txt
```

### 2. Running the Script

The main script `combinedIndia_code.py` contains functions like:

* `predict_fvc_weighted(age, height, weight, sex)`
* `predict_fev1_weighted(...)`

You can run predictions manually or use the batch CSV processing function.

### 3. Sample Usage

```python
from combinedIndia_code import predict_fvc_weighted

# Example input
age = 45
height = 170
weight = 65
sex = "male"

fvc = predict_fvc_weighted(age, height, weight, sex)
print("FVC (weighted):", fvc["pred"])
```

---

## 📁 Files

* `Indian_regions_combined.py` — Main prediction functions and regional model calls
* `README.md` — This guide
* `input_india.csv` — Input(average height and weight across India) for the python file

---

## 📊 Input Format for CSV

Columns expected:

```
age,height,weight,sex
45,170,65,male
32,158,60,female
```

---

## 📚 Notes

* Regional models are embedded inside the script and averaged using weights.
* Each region’s contribution is based on its sample size.
* LLN and ULN are included where available or estimated.

---

## 📝 License

MIT License
