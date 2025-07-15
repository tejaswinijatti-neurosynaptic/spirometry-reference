# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 16:37:35 2025

@author: Tejaswini
"""

import pandas as pd
import math

def lln_uln(pred, SD):
    lln = pred - 1.64 * SD
    uln = pred + 1.64 * SD
    return lln, uln

#The Open respiratory Medicine Journal_2023
def predict_fvc(age, height, weight, sex):
    sex = sex.strip()
    
    if sex == "Male":
        if age < 20: #male and below 20 years of age
            pred = 0.012 - 0.21296*age + 0.011291*(age**2) + 0.00017278*(height**2)
            SD = 1.233
        else: #male and above 20 years of age
            pred = -0.014 - 0.00264*(age) - 0.0002275*(age**2) + 0.00018221*(height**2)
            SD = 0.905
            
    elif sex == "Female":
        if age < 20: #female and below 20 years of age
            pred = -1.173 + 0.05817*(age) + 0.000224*(age**2) + 0.00014468*(height**2)
            SD= 0.780
        else: #female and above 20 years of age
            pred=0.029 + 0.00588*(age) - 0.0002559*(age**2) + 0.00014407*(height**2)
            SD=0.705      
    else:
        raise ValueError("Invalid sex")
    
    lln, uln = lln_uln(pred, SD)
    return round(pred,2), round(lln, 2), round(uln, 2)

def predict_fev1(age, height, weight, sex):
    sex = sex.strip()
    
    if sex == "Male":
        if age < 20:
            pred = -0.123 - 0.15548*(age) + 0.0087919*(age**2) + 0.00014659*(height**2)
            SD=1.061
        else:
            pred = 0.986 - 0.01653*(age) - 0.0001309*(age**2) + 0.00012975*(height**2)
            SD = 0.815
            
    elif sex == "Female":
        if age<20:
            pred = -1.261 + 0.09815*(age) - 0.0014096*(age**2) + 0.00020547*(height**2)
            SD = 0.693
        else:
            pred = 0.777 - 0.00921*(age) - 0.0001374*(age**2) + 0.00010647*(height**2)
            SD = 0.655
    else: 
        raise ValueError("Invalid sex")
        
    lln, uln = lln_uln(pred, SD)
    return round(pred,2), round(lln,2), round(uln,2)

def predict_pef(age, height, weight, sex):
    sex=sex.strip()
    
    if sex == "Male":
        if age<20:
            pred = 0.553 - 0.33295*(age) + 0.0220001*(age**2) + 0.00025096*(height**2)
            SD = 2.342
        else:
            pred = 1.047 + 0.07164*(age) - 0.0011848*(age**2) + 0.00025889*(height**2)
            SD = 1.946
    elif sex == "Female":
        if age<20:
            pred = -4.373 + 0.67357*(age) - 0.0201231*(age**2) + 0.00020547*(height**2)
            SD=1.521
        else:
            pred = 1.029 + 0.05084*(age) - 0.000844*(age**2) + 0.00019732*(height**2)
            SD = 1.467
    else:
        raise ValueError("Invalid sex")
        
    lln,uln=lln_uln(pred, SD)
    return round(pred,2), round(lln,2), round(uln,2)

def predict_fef75(age, weight, height, sex):
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

#Respiration_1999
def predict_tlc(height,weight, age, sex):
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

def predict_fef50(height, age, sex):
    sex = sex.strip()
    
    if sex == "Male": #converting height in cm to m
        pred = -1.71 + 5.28*(height/100) - 0.031*(age)
        SD = 0.59
    else:
        pred = -0.15 + 3.18*(height/100) - 0.013*(age)
        SD = 0.56
        
    lln, uln = lln_uln(pred, SD)
    return round(pred, 2), round(lln, 2), round(uln, 2)

def predict_fev1percent(height, age, weight, sex):
    sex= sex.strip()
    
    if sex == "Male": 
        if age<20: 
            pred = 71.2 + 0.121*height - 0.133*weight + 0.354*age
            SD = 6.14
        else:
            pred = 119 - 0.16*(height) - 0.28*(age)
            SD = 1.95
    elif sex == "Female":
        if age<20: 
            pred = 68.81 + 0.167*height - 0.147*weight + 0.227*age
            SD = 1.55
        else: 
            pred = 115 - 0.17*(height) - 0.22*(age)
            SD = 1.95
    else:
        raise ValueError("Invalid sex")
        
    lln, uln = lln_uln(pred, SD)
    return round(pred, 2), round(lln, 2), round(uln, 2)

def process_patient_data(file_path):
    df = pd.read_csv(file_path)

    fvc_preds, fvc_llns, fvc_ulns = [], [], []
    fev1_preds, fev1_llns, fev1_ulns = [], [], []
    pefr_preds, pefr_llns, pefr_ulns = [], [], []
    fev1percent_preds, fev1percent_llns, fev1percent_ulns = [], [], []
    fef50_preds, fef50_llns, fef50_ulns = [], [], []
    fef75_preds, fef75_llns, fef75_ulns = [], [], []
    tlc_preds, tlc_llns, tlc_ulns = [], [], []

    for _, row in df.iterrows():
        age = row['age']
        height = row['height_cm']
        weight = row['weight_kg']
        sex = row['sex']
        fvc_p, fvc_l, fvc_u = predict_fvc(age, height, weight, sex)
        fvc_preds.append(fvc_p)
        fvc_llns.append(fvc_l)
        fvc_ulns.append(fvc_u)

        fev1_p, fev1_l, fev1_u = predict_fev1(age, height, weight, sex)
        fev1_preds.append(fev1_p)
        fev1_llns.append(fev1_l)
        fev1_ulns.append(fev1_u)

        pefr_p, pefr_l, pefr_u = predict_pef(age, height, weight, sex)
        pefr_preds.append(pefr_p)
        pefr_llns.append(pefr_l)
        pefr_ulns.append(pefr_u)

        fev1p_p, fev1p_l, fev1p_u = predict_fev1percent(height, age, weight, sex)
        fev1percent_preds.append(fev1p_p)
        fev1percent_llns.append(fev1p_l)
        fev1percent_ulns.append(fev1p_u)

        fef50_p, fef50_l, fef50_u = predict_fef50(height, age, sex)
        fef50_preds.append(fef50_p)
        fef50_llns.append(fef50_l)
        fef50_ulns.append(fef50_u)

        fef75_p, fef75_l, fef75_u = predict_fef75(age, weight, height, sex)
        fef75_preds.append(fef75_p)
        fef75_llns.append(fef75_l)
        fef75_ulns.append(fef75_u)

        tlc_p, tlc_l, tlc_u = predict_tlc(height, weight, age, sex)
        tlc_preds.append(tlc_p)
        tlc_llns.append(tlc_l)
        tlc_ulns.append(tlc_u)

    df['FVC_pred'] = fvc_preds
    df['FVC_LLN'] = fvc_llns
    df['FVC_ULN'] = fvc_ulns

    df['FEV1_pred'] = fev1_preds
    df['FEV1_LLN'] = fev1_llns
    df['FEV1_ULN'] = fev1_ulns

    df['PEFR_pred'] = pefr_preds
    df['PEFR_LLN'] = pefr_llns
    df['PEFR_ULN'] = pefr_ulns

    df['FEV1%_pred'] = fev1percent_preds
    df['FEV1%_LLN'] = fev1percent_llns
    df['FEV1%_ULN'] = fev1percent_ulns

    df['FEF50_pred'] = fef50_preds
    df['FEF50_LLN'] = fef50_llns
    df['FEF50_ULN'] = fef50_ulns

    df['FEF75_pred'] = fef75_preds
    df['FEF75_LLN'] = fef75_llns
    df['FEF75_ULN'] = fef75_ulns

    df['TLC_pred'] = tlc_preds
    df['TLC_LLN'] = tlc_llns
    df['TLC_ULN'] = tlc_ulns

    return df

if __name__ == "__main__": #Replace the input file directory
    input_file = r"d:\Users\Tejaswini\Desktop\neurosyn\mexican american\input_tej.csv" 
    output_file = "spirometry_predictions_mexicanamerican.csv"

    df_result = process_patient_data(input_file)
    df_result.to_csv(output_file, index=False)

    
    
        
        
        
    