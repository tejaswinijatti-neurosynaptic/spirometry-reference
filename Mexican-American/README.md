# Mexican American Spirometry Reference Calculator

This folder contains Python code and documentation for calculating spirometry reference values specific to the **Mexican American** population. The reference equations are based on NHANES III and peer-reviewed literature focused on individuals of Mexican descent residing in the United States.

---

## 📄 Overview
- **Parameters Covered**: FVC, FEV1, FEV1/FVC%, PEFR, TLC, FEF25–75, FEF50, FEF75
- **Age Range**: 5 to 95 years
- **Population**: Mexican Americans (based on NHANES III data)
- **Regression Models**: Linear and quadratic models

---

## 🚀 Getting Started

### 1. Requirements
Install required Python libraries:
```bash
pip install -r ../requirements.txt
```

### 2. Sample Usage
```python
from spirometry_mexican import predict_fev1, predict_fvc

age = 45
height = 170
sex = "male"

fev1 = predict_fev1(age, height, sex)
fvc = predict_fvc(age, height, sex)
print("FEV1:", fev1)
print("FVC:", fvc)
```

---

## 📁 Files
- `spirometry_mexican.py`: Contains prediction functions
-  `input.csv`: Contains sample input values for the code
- `README.md`: This guide
- `whitepaper_mexican.pdf`: Full documentation on population, data sources, and methodology

---

## 📚 References
1. Hankinson JL, et al. NHANES III spirometry reference values. [PubMed](https://www.ncbi.nlm.nih.gov/articles/PMC10351349/)
2. Quanjer PH, et al. Total lung capacity in children. [AnnalsATS](https://www.atsjournals.org/doi/epdf/10.1513/AnnalsATS.201712-922OC?role=tab)
3. Stocks J, et al. TLC for adults. [Acta Medica](https://sci-hub.se/10.1159/000209385)
4. Perez-Padilla R, et al. FEF equations. [Arc Med](https://sci-hub.se/10.1016/j.arcmed.2004.06.010)

---

## 📝 License
MIT License
