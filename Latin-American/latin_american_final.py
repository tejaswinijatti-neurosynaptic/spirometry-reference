# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 16:00:37 2025

@author: Tejaswini
"""

import pandas as pd
import math
import numpy as np

def lln_uln(pred, SD):
    lln = pred - 1.64 * SD
    uln = pred + 1.64 * SD
    return lln, uln

#from https://doi.org/10.1016/j.arbres.2019.12.033
def lms_lln_uln(L, M, S, Z):
    """Calculate percentile using LMS method."""
    if L == 0:
        return M * np.exp(S * Z)
    else:
        return M * ((1 + L * S * Z) ** (1 / L))

# MALES (LMS model)
def predict_male_fev1(age, height):
    # L equation
    L = 0.37 * math.log(age) - 0.22
    # M equation (lnFEV1)
    ln_M = 2.0468*math.log(height) + 0.0236*math.log(age) - 9.2954
    M = np.exp(ln_M)
    # S equation
    ln_S = 0.108 * math.log(age) - 2.430
    S = np.exp(ln_S)
    fev1_pred = M
    fev1_lln = lms_lln_uln(L, M, S, -1.645)
    fev1_uln = lms_lln_uln(L, M, S, 1.645)
    return round(fev1_pred,2), round(fev1_lln,2), round(fev1_uln,2)

def predict_male_fvc(age, height):
    # L equation
    L = 0.34 * math.log(age) - 0.36
    # M equation (lnFVC)
    ln_M = 2.174*math.log(height) + 0.071*math.log(age) - 9.913
    M = np.exp(ln_M)
    # S equation
    ln_S = 0.0094 * age - 2.424
    S = np.exp(ln_S)
    fvc_pred = M
    fvc_lln = lms_lln_uln(L, M, S, -1.645)
    fvc_uln = lms_lln_uln(L, M, S, 1.645)
    return round(fvc_pred,2), round(fvc_lln,2), round(fvc_uln,2)

def predict_male_fev1_fvc(age, height):
    # L equation
    L = 0.34 * math.log(age) + 2.25
    # M equation (lnFEV1/FVC)
    M = -0.0478*height - 4.3828*math.log(age) + 105.5463
    # S equation
    S = 0.00119 * math.log(age) + 0.05870
    fev1_fvc_pred = M
    fev1_fvc_lln = lms_lln_uln(L, M, S, -1.645)
    fev1_fvc_uln = lms_lln_uln(L, M, S, 1.645)
    return round(fev1_fvc_pred,2), round(fev1_fvc_lln,2), round(fev1_fvc_uln,2)

# FEMALES (Linear regression)
# Standard deviation (SD) values for FEV1, FVC, FEV1/FVC
SD_fev1_female = 0.21
SD_fvc_female = 0.22
SD_fev1_fvc_female = 0.058

def predict_female_fev1(age, height):
    ln_fev1 = (0.0575872 * height - 0.0001315 * height**2 + 0.0098811 * age - 0.0002149 * age**2 - 4.7751014)
    fev1_pred = np.exp(ln_fev1)
    fev1_lln = fev1_pred - 1.645 * SD_fev1_female
    fev1_uln = fev1_pred + 1.645 * SD_fev1_female
    return round(fev1_pred,2), round(fev1_lln,2), round(fev1_uln,2)

def predict_female_fvc(age, height):
    ln_fvc = (0.0505208 * height - 0.0001110 * height**2 + 0.0140743 * age - 0.0002325 * age**2 - 4.1232304)
    fvc_pred = np.exp(ln_fvc)
    fvc_lln = fvc_pred - 1.645 * SD_fvc_female
    fvc_uln = fvc_pred + 1.645 * SD_fvc_female
    return round(fvc_pred,2), round(fvc_lln,2), round(fvc_uln,2)

def predict_female_fev1_fvc(age, height):
    ln_ratio = (0.0010022 * height - 0.0029468 * age + 4.3845851)
    fev1_fvc_pred = np.exp(ln_ratio)
    fev1_fvc_lln = fev1_fvc_pred - 1.645 * SD_fev1_fvc_female
    fev1_fvc_uln = fev1_fvc_pred + 1.645 * SD_fev1_fvc_female
    return round(fev1_fvc_pred,2), round(fev1_fvc_lln,2), round(fev1_fvc_uln,2)

#from 10.15446/revfacmed.v66n2.63571
def predict_fef2575_male(age, height):
    pred = -0.03*age +0.05*height
    SD = 0.84
    lln, uln = lln_uln(pred, SD)
    return round(pred,2), round(lln, 2), round(uln, 2)
def predict_fef2575_female(age, height):
    pred = -0.03*age +0.03*height
    SD = 0.63
    lln, uln = lln_uln(pred, SD)
    return round(pred,2), round(lln, 2), round(uln, 2)

#https://doi.org/10.1590/s1806-37132007000400008 
def predict_fef50_brazil(age, height, sex):
    sex = sex.strip()
    if sex == "Male":
        ln_pred = 0.839 * math.log(height) - 0.404 * math.log(age) - 1.369
        SD = 1.44
    elif sex == "Female":
        ln_pred = 0.839 * math.log(height) - 0.404 * math.log(age) - 1.369
        SD = 1.14
    else:
        raise ValueError("Invalid sex")
    pred = math.exp(ln_pred)
    lln, uln = lln_uln(pred, SD)
    return round(pred,2), round(lln,2), round(uln,2)

#10.1016/j.arcmed.2004.06.010
def predict_fef50_mex(height, age, sex): #n=436
    sex = sex.strip()
    
    if sex == "Male": #converting height in cm to m
        pred = -1.71 + 5.28*(height/100) - 0.031*(age)
        SD = 0.59
    else:
        pred = -0.15 + 3.18*(height/100) - 0.013*(age)
        SD = 0.56
        
    lln, uln = lln_uln(pred, SD)
    return round(pred, 2), round(lln, 2), round(uln, 2)

def predict_fef50_weighted(age, height, sex):
    pred_mex, lln_mex, uln_mex = predict_fef50_mex(height, age, sex)
    pred_brz, lln_brz, uln_brz = predict_fef50_brazil(age, height, sex)
    w_mex = 436
    w_brz = 643
    total = w_mex + w_brz
    pred_weighted = (pred_mex * w_mex + pred_brz * w_brz) / total
    lln_weighted = (lln_mex * w_mex + lln_brz * w_brz) / total
    uln_weighted = (uln_mex * w_mex + uln_brz * w_brz) / total
    return round(pred_weighted, 2), round(lln_weighted, 2), round(uln_weighted, 2)

#http://dx.doi.org/10.1590/1414-431X20175700
def predict_fef75_brazil(age, height, sex):
    sex = sex.strip()
    if sex == "Male":
        pred = -0.0328 * age + 0.0175 * height + 0.0140
        SD = 0.5791
    elif sex == "Female":
        pred = -0.0220 * age + 0.0153 * height + 0.1543
        SD = 0.4365
    else:
        raise ValueError("Invalid sex")
    lln, uln = lln_uln(pred, SD)
    return round(pred,2), round(lln,2), round(uln,2)

#10.1016/j.arcmed.2004.06.010
def predict_fef75_mex(age, weight, height, sex): #n=436
    sex=sex.strip()
    
    if sex == "Male":
        pred = -5.90 + 5.55*(height/100) - 0.019*age
        SD = 0.28
    elif sex == "Female":
        pred = 1.46 + 1.05*(height/100) - 0.026*age
        SD= 0.44
    else:
        raise ValueError("Invalid sex")
        
    lln, uln = lln_uln(pred, SD)
    return round(pred,2), round(lln,2), round(uln,2)

# Combine FEF75 predictions from Mexico and Brazil using weighted mean.
#Mexico: n = 436, Brazil: n = 454
def predict_fef75_weighted(age, height, weight, sex):
    pred_mex, lln_mex, uln_mex = predict_fef75_mex(age, weight, height, sex)
    pred_brz, lln_brz, uln_brz = predict_fef75_brazil(age, height, sex)
    w_mex = 436
    w_brz = 454
    total = w_mex + w_brz
    pred_weighted = (pred_mex * w_mex + pred_brz * w_brz) / total
    lln_weighted = (lln_mex * w_mex + lln_brz * w_brz) / total
    uln_weighted = (uln_mex * w_mex + uln_brz * w_brz) / total
    return round(pred_weighted, 2), round(lln_weighted, 2), round(uln_weighted, 2)

#https://dx.doi.org/10.36416/1806-3756/e20200359 Brazil
def predict_tlc_brazil(age, height, sex):
    sex = sex.strip()
    if sex == "Male":
        pred = 0.081 * height - 7.404
        SD = 0.61
    elif sex == "Female":
        pred = 0.057 * height - 4.205
        SD = 0.50
    else:
        raise ValueError("Invalid sex")
    lln, uln = lln_uln(pred, SD)
    return round(pred,2), round(lln,2), round(uln,2)

#https://doi.org/10.1159/000029385 Mexican
def predict_tlc_mex(height,weight, age, sex):
    sex= sex.strip()
    
    if sex == "Male":
        if age <20:
            ln_pred = 0.02907*(age) + 0.00977*(height) + 0.00287*(weight) - 0.57111
            pred = math.exp(ln_pred)
            SD = 0.13318
        else:
            pred = 0.106*(height) - 11.369
            SD = 0.68
    elif sex == "Female":
        if age<20:
            ln_pred = 0.01732*(age) + 0.01012*(height) + 0.00387*(weight) - 0.63712
            pred = math.exp(ln_pred)
            SD = 0.12879
        else:
            pred= 0.072*(height) - 0.009*(age) - 6.125
            SD = 0.54
    else:
        raise ValueError("Invalid sex")
    lln, uln= lln_uln(pred, SD)
    return round(pred, 2), round(lln, 2), round(uln, 2)

# Combines TLC predictions from Mexico and Brazil using weighted mean.
#Weights: Mexico (n=591), Brazil (n=244)
def predict_tlc_weighted(age, height, weight, sex):
    # Individual predictions
    pred_mex, lln_mex, uln_mex = predict_tlc_mex(height, weight, age, sex)
    pred_brz, lln_brz, uln_brz = predict_tlc_brazil(age, height, sex)
    # Weights
    w_mex = 591
    w_brz = 244
    total = w_mex + w_brz
    # Weighted average
    pred_weighted = (pred_mex * w_mex + pred_brz * w_brz) / total
    lln_weighted = (lln_mex * w_mex + lln_brz * w_brz) / total
    uln_weighted = (uln_mex * w_mex + uln_brz * w_brz) / total
    return round(pred_weighted, 2), round(lln_weighted, 2), round(uln_weighted, 2)

#https://doi.org/10.1157/13090581
def predict_pefr(age, height, sex):
    sex= sex.strip()
    if sex == "Male":
        pred = -0.07185995*age + 0.06294803*height + 2.4914045
        SD = 1.123243
    elif sex == "Female":
        pred = -0.05360108*age + 0.05653161*height + 0.65195532
        SD = 1.123243
    else:
        raise ValueError("Invalid sex")
    lln, uln = lln_uln(pred, SD)
    return round(pred,2), round(lln,2), round(uln,2)

def process_patient_data(file_path):
    df = pd.read_csv(file_path)
    results = []

    for _, row in df.iterrows():
        age = row["age"]
        height = row["height_cm"]
        weight = row.get("weight_kg") 
        sex = row["sex"].strip()

        if sex == "Male":
            fev1, fev1_lln, fev1_uln = predict_male_fev1(age, height)
            fvc, fvc_lln, fvc_uln = predict_male_fvc(age, height)
            fev1_fvc, fev1_fvc_lln, fev1_fvc_uln = predict_male_fev1_fvc(age, height)
        elif sex == "Female":
            fev1, fev1_lln, fev1_uln = predict_female_fev1(age, height)
            fvc, fvc_lln, fvc_uln = predict_female_fvc(age, height)
            fev1_fvc, fev1_fvc_lln, fev1_fvc_uln = predict_female_fev1_fvc(age, height)
        else:
            raise ValueError(f"Invalid sex: {sex}")

        fef2575, fef2575_lln, fef2575_uln = (
            predict_fef2575_male(age, height) if sex == "Male" else predict_fef2575_female(age, height)
        )

        #Use weighted versions
        fef50, fef50_lln, fef50_uln = predict_fef50_weighted(age, height, sex)
        fef75, fef75_lln, fef75_uln = predict_fef75_weighted(age, height, weight, sex)
        tlc, tlc_lln, tlc_uln = predict_tlc_weighted(age, height, weight, sex)
        pefr, pefr_lln, pefr_uln = predict_pefr(age, height, sex)

        results.append({
            "Age": age,
            "Height": height,
            "Weight": weight,
            "Sex": sex,

            "FEV1_pred": fev1,
            "FEV1_LLN": fev1_lln,
            "FEV1_ULN": fev1_uln,

            "FVC_pred": fvc,
            "FVC_LLN": fvc_lln,
            "FVC_ULN": fvc_uln,

            "FEV1/FVC_pred": fev1_fvc,
            "FEV1/FVC_LLN": fev1_fvc_lln,
            "FEV1/FVC_ULN": fev1_fvc_uln,

            "FEF25-75_pred": fef2575,
            "FEF25-75_LLN": fef2575_lln,
            "FEF25-75_ULN": fef2575_uln,

            "FEF50_pred": fef50,
            "FEF50_LLN": fef50_lln,
            "FEF50_ULN": fef50_uln,

            "FEF75_pred": fef75,
            "FEF75_LLN": fef75_lln,
            "FEF75_ULN": fef75_uln,

            "TLC_pred": tlc,
            "TLC_LLN": tlc_lln,
            "TLC_ULN": tlc_uln,

            "PEFR_pred": pefr,
            "PEFR_LLN": pefr_lln,
            "PEFR_ULN": pefr_uln,
        })

    return pd.DataFrame(results)

if __name__ == "__main__":
    input_file = r"d:\Users\Tejaswini\Desktop\neurosyn\Demo\latinamerican_input.csv" 
    output_file = r"d:\Users\Tejaswini\Desktop\neurosyn\Demo\spirometry_predictions_latinamerican.csv"

    df_result = process_patient_data(input_file)
    columns_to_clip = [
    "FEV1_pred", "FEV1_LLN", "FEV1_ULN",
    "FVC_pred", "FVC_LLN", "FVC_ULN",
    "FEV1/FVC_pred", "FEV1/FVC_LLN", "FEV1/FVC_ULN",
    "FEF25-75_pred", "FEF25-75_LLN", "FEF25-75_ULN",
    "FEF50_pred", "FEF50_LLN", "FEF50_ULN",
    "FEF75_pred", "FEF75_LLN", "FEF75_ULN",
    "TLC_pred", "TLC_LLN", "TLC_ULN",
    "PEFR_pred", "PEFR_LLN", "PEFR_ULN"]
for col in columns_to_clip:
    if col in df_result.columns:
        df_result[col] = df_result[col].clip(lower=0)
        
    df_result.to_csv(output_file, index=False)

    
    
        
        
        
    