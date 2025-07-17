# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 17:02:08 2025

@author: Tejaswini
"""

import pandas as pd
import math
import numpy as np

def lln_uln(pred, SD):
    lln = pred - 1.64 * SD
    uln = pred + 1.64 * SD
    return lln, uln

def fvc_eastern(height, weight, age, sex):
    if sex == "Male":
        pred =-0.0214*age + 0.0522*height + -4.129
        SD = 0.45
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)
    elif sex == "Female":
        pred = -0.025*age + 0.027*height - 0.902
        SD = 0.31
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)
    else: None

def fev1_eastern(height, age, sex):
    if sex == "Male":
        pred = -0.0286*age + 0.0533*height - 4.6899
        SD = 0.42
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)
    elif sex == "Female":
        pred = -0.027*age + 0.021*height - 0.254
        SD = 0.284
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)

def fev1_fvc_eastern(height, age, sex):
    if sex == "Male":
        pred = -.3093*age + 0.2136*height + 58.76
        SD = 6.81
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)
    elif sex == "Female":
        pred = -0.241*age + 86.1
        SD = 5.680
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)

def pefr_eastern(height, age, sex):
    if sex == "Male":
        pred = -3.6350*age + 0.2136*height + 358.8
        SD = 55.74
    elif sex == "Female":
        pred = -2.951*age + 532.203
        SD = 48.379
    else:
        return None, None, None
    # Convert from L/min to L/sec by dividing by 60
    pred_lps = pred / 60.0
    SD_lps = SD / 60.0 # Standard Deviation also needs conversion

    lln_lps, uln_lps = lln_uln(pred_lps, SD_lps)
    return round(pred_lps,2), round(lln_lps, 2), round(uln_lps, 2)

def fef75_eastern(height, age, sex):
    if sex == "Male":
        pred = -1.4098*age + 0.6777*height + 7.637
        SD = 6.13
    elif sex == "Female":
        pred = -2.956*age + 0*height + 196.668
        SD = 6.13
    # Convert from L/min to L/sec by dividing by 60
    pred_lps = pred / 60.0
    SD_lps = SD / 60.0

    lln_lps, uln_lps = lln_uln(pred_lps, SD_lps)
    return round(pred_lps,2), round(lln_lps, 2), round(uln_lps, 2)

def fef25_75_eastern_female(age, height, sex):
    if sex == "Male":
        pred = -2.7877*age + 3.6742*height - 263.62
        SD = 56.89
    elif sex == "Female":
        pred = -2.71*age + 258.246
        SD = 49.43
    else:
        return None
    # Convert from L/min to L/sec by dividing by 60
    pred_lps = pred / 60.0
    SD_lps = SD / 60.0

    lln_lps, uln_lps = lln_uln(pred_lps, SD_lps)
    return round(pred_lps,2), round(lln_lps, 2), round(uln_lps, 2)

def fvc_northern(height, weight, age, sex):
    if sex == "Male":
        pred = -5.048 + (-0.014 * age) + (0.054 * height) + (0.006 * weight)
        SD = 0.479
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)
    elif sex == "Female": 
        pred = 20.07 + (-0.010 * age) + (-0.261 * height) + (0.000972 * height ** 2)
        SD = 0.315
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)

def fev1_northern(age, height, sex):
    if sex == "Male":
        pred= -3.682 + (-0.024 * age) + (0.046 * height)
        SD = 0.402
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)
    elif sex == "Female": 
        pred= -2.267 + (-0.019 * age) + (0.033 * height)
        SD = 0.286
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)

def pefr_northern(age, height, sex):
    if sex == "Male":
        ln_pred = 0.346 + (-0.004 * age) + (0.011 * height)
        pred = math.exp(ln_pred)
        SD = 0.158
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)
    elif sex == "Female": 
        pred = -0.829 + (0.0137 * height) + (0.026 * age) - (0.000402 * age ** 2)
        SD = 0.198
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)  

def fev1_fvc_northern(age, weight, sex):
    if sex == "Male":
        pred = 102.56 + (-0.679 * age) + (0.00477*(age**2))+(-0.08 * weight)
        SD = 5.79
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)
    elif sex == "Female": 
        pred= 97.182 + (-0.44 * age)
        SD = 0.286
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)

def fef50_northern(age, height, sex):
    if sex == "Male":
        ln_pred = 0.573 - (0.016 * age) + (0.008 * height)
        pred = math.exp(ln_pred)
        SD = 0.262
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)
    elif sex == "Female": 
        ln_pred = -0.051 + (0.010 * height) - (0.015 * age)
        pred = math.exp(ln_pred)
        SD = 0.292   
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)    

def fef75_northern(age, height, weight, sex):
    if sex == "Male":
        ln_pred = -0.584 - (0.055 * age) + (0.015 * height)-(0.005*weight)+(0.000318*age**2)
        pred = math.exp(ln_pred)
        SD = 0.249
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)
    elif sex == "Female": 
        pred = 0.423 - (0.09 * age) + (0.000799 * age**2) + (0.017 * height)
        SD = 0.251    
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)    

def estimate_sd(pred, rsd_percent):
    SD = (rsd_percent / 100) * pred
    return SD

def fev1_southern(height, age, weight, sex):
    if sex == "Male":
        pred =  -1.969+(0.039*height)-(0.026*age)-(0.008*weight)
        rsd = 0.379
        SD = estimate_sd(pred, rsd)
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)
    elif sex == "Female":
        pred = -1.287+(0.025*height)-(0.018*age)
        rsd = 0.259
        SD = estimate_sd(pred, rsd)
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)

def fvc_southern(height, age, weight, sex):
    if sex == "Male":
        pred = -2.207+(0.045*height)-(0.027*age)-(0.009*weight)
        rsd = 0.435
        SD = estimate_sd(pred, rsd)
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)
    elif sex == "Female":
        pred = -2.207+(0.034*height)-(0.017*age)
        rsd = 0.299
        SD = estimate_sd(pred, rsd)
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)

def fev1_fvc_southern(age, sex):
    if sex == "Male":
        pred = 111.281-(1.068*age)+(0.009*age**2)
        rsd = 5.416
        SD = estimate_sd(pred, rsd)
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)
        return round(pred,2), round(lln, 2), round(uln, 2)
    elif sex == "Female":
        pred = 90.042-(0.184*age)
        rsd = 5.626
        SD = estimate_sd(pred, rsd)
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)

def fev1_western(age, height, sex):
    if sex == "Female":
        pred = np.exp(-0.6439556 - 0.0066921 * age + 0.0104873 * height)
        SD = np.exp(-2.911064 + 0.017174*age)
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)
    elif sex == "Male":
        pred = 0.402779 - 0.021695 * age + 0.019853 * height
        SD = 0.413964
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)
    
def fvc_western(age, height, sex):
    if sex == "Female":
        pred = np.exp(-0.5590106 - 0.0040786 * age + 0.0105529 * height)
        SD = np.exp(-2.235059 + 0.007378*age)
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)
    if sex == "Male":
        pred = -0.038933 - 0.016466 * age + 0.025120 * height
        SD = 0.473403
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)

def fev1_fvc_western(age, height, sex):
    if sex == "Female":
        pred = (0.905877 - 0.002132 * age)*100
        SD = 6.0512
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)
    if sex == "Male":
        pred = (0.922257 - 0.002695 * age)*100
        SD = 5.9375
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)

def fvc_kashmiri(age, height, sex):
    if sex == "Male":
        if age <= 30:
            pred = -0.021*age + 0.032*height - 0.416
            SD = 0.685
        elif age <= 50:
            pred = -0.005*age + 0.025*height + 0.411
            SD = 0.671
        else:
            pred = -0.031*age + 0.040*height - 1.747
            SD = 0.589
    elif sex == "Female":
        if age <= 30:
            pred = -0.022*age + 0.022*height + 0.244
            SD = 0.454
        elif age <= 50:
            pred = -0.004*age + 0.016*height + 0.508
            SD = 0.446
        else:
            pred = -0.002*age + 0.022*height - 0.772
            SD = 0.442
    lln, uln = lln_uln(pred, SD)
    return round(pred,2), round(lln, 2), round(uln, 2)


def fev1_kashmiri(age, height, sex):
    if sex =="Male":
        if age <= 30:
            pred = -0.015*age + 0.023*height - 0.468
            SD = 0.448
        elif age <= 50:
            pred = -0.004*age + 0.017*height + 0.063
            SD = 0.416
        else:
            pred = -0.004*age + 0.017*height + 0.063
            SD = 0.41
    elif sex == "Female":
        if age <= 30:
            pred = -0.014*age + 0.033*height - 1.136
            SD = 0.627
        elif age <= 50:
            pred = -0.005*age + 0.023*height + 0.242
            SD = 0.634
        else:
            pred = -0.030*age + 0.037*height - 1.483
            SD = 0.563
    lln, uln = lln_uln(pred, SD)
    return round(pred,2), round(lln, 2), round(uln, 2)

def fev1_fvc_kashmiri(age, height, sex):
    if sex == "Male":
        if age <= 30:
            pred = 0.106*age + 0.089*height + 72.742
            SD = 2.897
        elif age <= 50:
            pred = -0.004*age + 0.026*height + 85.516
            SD = 2.722
        else:
            pred = -0.021*age + 0.147*height + 54.976
            SD = 2.56
    elif sex == "Female":
        if age <= 30:
            pred = 0.137*age + 0.105*height + 67.8
            SD = 3.139
        elif age <= 50:
            pred = 0.012*age + 0.077*height + 75.836
            SD = 3.095
        else:
            pred = -0.021*age + 0.205*height + 54.976
            SD = 3.166
    lln, uln = lln_uln(pred, SD)
    return round(pred,2), round(lln, 2), round(uln, 2)


def fef25_75_kashmiri(age, height, sex):
    if sex == "Male":
        if age <= 30:
            pred = 0.003*age + 0.038*height - 2.041
            SD = 1.076
        elif age <= 50:
            pred = 0.002*age + 0.019*height + 0.631
            SD = 0.862
        else:
            pred = 0.041*age + 0.051*height + 3.109
            SD = 0.969
    elif sex == "Female":
        if age <= 30:
            pred = -0.012*age + 0.031*height - 1.130
            SD = 0.687
        elif age <= 50:
            pred = -0.003*age + 0.008*height + 2.004
            SD = 0.714
        else:
            pred = 0.011*age - 0.021*height + 5.376
            SD = 0.692
    lln, uln = lln_uln(pred, SD)
    return round(pred,2), round(lln, 2), round(uln, 2)
    
def pefr_kashmiri(age, height, sex):
    if sex == "Male":
        if age <= 30:
            pred = -0.007*age + 0.053*height - 0.517
            SD = 1.744
        elif age <= 50:
            pred = -0.009*age + 0.043*height - 1.368
            SD = 1.695
        else:
            pred = -0.041*age + 0.060*height - 1.122
            SD = 1.45
    elif sex == "Female":
        if age <= 30:
            pred = 0.009*age + 0.017*height + 0.211
            SD = 0.62
        elif age <= 50:
            pred = -0.002*age + 0.007*height - 2.900
            SD = 0.547
        else:
            pred = 0.008*age + 0.033*height - 2.900
            SD = 0.646
    lln, uln = lln_uln(pred, SD)
    return round(pred,2), round(lln, 2), round(uln, 2)

def fvc_northeast(age, height, sex):
    if sex == "Male":
        pred = -0.024 * age + 0.024 * height + 0.003
        SD = 0.448
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)
    elif sex == "Female":
        pred = -0.021 * age + 0.014 * height + 0.687
        SD = 0.359
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)

def fev1_northeast(age, height, sex):
    if sex == "Male":
        pred = -0.025 * age + 0.020 * height + 0.269
        SD = 0.46
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)
    elif sex == "Female":
        pred = -0.021 * age + 0.011 * height + 0.770
        SD = 0.356
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)

def pef_northeast(age, height, sex):
    if sex == "Male":
        pred = -0.044 * age + 0.033 * height + 3.052
        SD = 1.69
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)
    elif sex == "Female":
        pred = -0.049 * age + 0.048 * height - 0.726
        SD = 1.381
        lln, uln = lln_uln(pred, SD)
        return round(pred,2), round(lln, 2), round(uln, 2)

weights = {"Male": {"north": 489, "south": 214, "east": 334, "west": 564, "kashmir": 636, "northeast": 0}, # Added northeast with 0 weight for now
        "Female": {"north": 196, "south": 369, "east": 230, "west": 694, "kashmir": 1338, "northeast": 0} } # Added northeast with 0 weight for now


def fvc_weighted(age, height, weight, sex):
    region_funcs = {
        "north": lambda: fvc_northern(height, weight, age, sex),
        "south": lambda: fvc_southern(height, age, weight, sex),
        "east": lambda: fvc_eastern(height, weight, age, sex),
        "west": lambda: fvc_western(age, height, sex),
        "kashmir": lambda: fvc_kashmiri(age, height, sex),
        "northeast": lambda: fvc_northeast(age, height, sex)
    }

    pred_sum = lln_sum = uln_sum = total_w = 0

    for region, func in region_funcs.items():
        try:
            pred, lln, uln = func()
            w = weights[sex].get(region, 0) # Use .get with default 0 in case region not in weights
            pred_sum += pred * w
            lln_sum += lln * w
            uln_sum += uln * w
            total_w += w
        except Exception as e:
            # print(f"Skipping region {region} for {sex} due to error: {e}") # For debugging
            continue  # Skip regions if function errors or sex data not available

    if total_w == 0:
        return None, None, None

    pred_w = pred_sum / total_w
    lln_w = lln_sum / total_w
    uln_w = uln_sum / total_w

    return round(pred_w, 2), round(lln_w, 2), round(uln_w, 2)

# New functions for weighted averages for FEV1, FEV1/FVC, PEFR, FEF25-75, FEF50, FEF75
def fev1_weighted(age, height, weight, sex):
    region_funcs = {
        "north": lambda: fev1_northern(age, height, sex),
        "south": lambda: fev1_southern(height, age, weight, sex),
        "east": lambda: fev1_eastern(height, age, sex),
        "west": lambda: fev1_western(age, height, sex),
        "kashmir": lambda: fev1_kashmiri(age, height, sex),
        "northeast": lambda: fev1_northeast(age, height, sex)
    }

    pred_sum = lln_sum = uln_sum = total_w = 0

    for region, func in region_funcs.items():
        try:
            pred, lln, uln = func()
            w = weights[sex].get(region, 0)
            pred_sum += pred * w
            lln_sum += lln * w
            uln_sum += uln * w
            total_w += w
        except Exception as e:
            # print(f"Skipping region {region} for {sex} due to error: {e}")
            continue

    if total_w == 0:
        return None, None, None

    pred_w = pred_sum / total_w
    lln_w = lln_sum / total_w
    uln_w = uln_sum / total_w

    return round(pred_w, 2), round(lln_w, 2), round(uln_w, 2)

def fev1_fvc_weighted(age, height, weight, sex):
    region_funcs = {
        "north": lambda: fev1_fvc_northern(age, weight, sex),
        "south": lambda: fev1_fvc_southern(age, sex),
        "east": lambda: fev1_fvc_eastern(height, age, sex),
        "west": lambda: fev1_fvc_western(age, height, sex),
        "kashmir": lambda: fev1_fvc_kashmiri(age, height, sex)
    }

    pred_sum = lln_sum = uln_sum = total_w = 0

    for region, func in region_funcs.items():
        try:
            pred, lln, uln = func()
            w = weights[sex].get(region, 0)
            pred_sum += pred * w
            lln_sum += lln * w
            uln_sum += uln * w
            total_w += w
        except Exception as e:
            # print(f"Skipping region {region} for {sex} due to error: {e}")
            continue

    if total_w == 0:
        return None, None, None

    pred_w = pred_sum / total_w
    lln_w = lln_sum / total_w
    uln_w = uln_sum / total_w

    return round(pred_w, 2), round(lln_w, 2), round(uln_w, 2)

def pefr_weighted(age, height, sex):
    region_funcs = {
        "north": lambda: pefr_northern(age, height, sex),
        "east": lambda: pefr_eastern(height, age, sex),
        "kashmir": lambda: pefr_kashmiri(age, height, sex),
        "northeast": lambda: pef_northeast(age, height, sex)
    }

    pred_sum = lln_sum = uln_sum = total_w = 0

    for region, func in region_funcs.items():
        try:
            pred, lln, uln = func()
            w = weights[sex].get(region, 0)
            pred_sum += pred * w
            lln_sum += lln * w
            uln_sum += uln * w
            total_w += w
        except Exception as e:
            # print(f"Skipping region {region} for {sex} due to error: {e}")
            continue

    if total_w == 0:
        return None, None, None

    pred_w = pred_sum / total_w
    lln_w = lln_sum / total_w
    uln_w = uln_sum / total_w

    return round(pred_w, 2), round(lln_w, 2), round(uln_w, 2)

def fef25_75_weighted(age, height, sex):
    region_funcs = {
        "east": lambda: fef25_75_eastern_female(age, height, sex),
        "kashmir": lambda: fef25_75_kashmiri(age, height, sex)
    }

    pred_sum = lln_sum = uln_sum = total_w = 0

    for region, func in region_funcs.items():
        try:
            pred, lln, uln = func()
            w = weights[sex].get(region, 0)
            pred_sum += pred * w
            lln_sum += lln * w
            uln_sum += uln * w
            total_w += w
        except Exception as e:
            # print(f"Skipping region {region} for {sex} due to error: {e}")
            continue

    if total_w == 0:
        return None, None, None

    pred_w = pred_sum / total_w
    lln_w = lln_sum / total_w
    uln_w = uln_sum / total_w

    return round(pred_w, 2), round(lln_w, 2), round(uln_w, 2)

def fef50_weighted(age, height, sex):
    region_funcs = {
        "north": lambda: fef50_northern(age, height, sex)
    }

    pred_sum = lln_sum = uln_sum = total_w = 0

    for region, func in region_funcs.items():
        try:
            pred, lln, uln = func()
            w = weights[sex].get(region, 0)
            pred_sum += pred * w
            lln_sum += lln * w
            uln_sum += uln * w
            total_w += w
        except Exception as e:
            # print(f"Skipping region {region} for {sex} due to error: {e}")
            continue

    if total_w == 0:
        return None, None, None

    pred_w = pred_sum / total_w
    lln_w = lln_sum / total_w
    uln_w = uln_sum / total_w

    return round(pred_w, 2), round(lln_w, 2), round(uln_w, 2)

def fef75_weighted(age, height, weight, sex):
    region_funcs = {
        "east": lambda: fef75_eastern(height, age, sex),
        "north": lambda: fef75_northern(age, height, weight, sex)
    }

    pred_sum = lln_sum = uln_sum = total_w = 0

    for region, func in region_funcs.items():
        try:
            pred, lln, uln = func()
            w = weights[sex].get(region, 0)
            pred_sum += pred * w
            lln_sum += lln * w
            uln_sum += uln * w
            total_w += w
        except Exception as e:
            # print(f"Skipping region {region} for {sex} due to error: {e}")
            continue

    if total_w == 0:
        return None, None, None

    pred_w = pred_sum / total_w
    lln_w = lln_sum / total_w
    uln_w = uln_sum / total_w

    return round(pred_w, 2), round(lln_w, 2), round(uln_w, 2)


# Function to process the input file
def process_lung_function_data(input_file_path, output_file_path):
    try:
        df = pd.read_csv(input_file_path)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file_path}' not found.")
        return
    except Exception as e:
        print(f"Error reading input file: {e}")
        return

    results = []

    for index, row in df.iterrows():
        sex = row['sex']
        height_cm = row['height_cm']
        age = row['age']
        weight_kg = row['weight_kg']

        # Calculate weighted averages for each lung function parameter
        fvc_pred, fvc_lln, fvc_uln = fvc_weighted(age, height_cm, weight_kg, sex)
        fev1_pred, fev1_lln, fev1_uln = fev1_weighted(age, height_cm, weight_kg, sex)
        fev1_fvc_pred, fev1_fvc_lln, fev1_fvc_uln = fev1_fvc_weighted(age, height_cm, weight_kg, sex)
        pefr_pred, pefr_lln, pefr_uln = pefr_weighted(age, height_cm, sex)
        fef25_75_pred, fef25_75_lln, fef25_75_uln = fef25_75_weighted(age, height_cm, sex)
        fef50_pred, fef50_lln, fef50_uln = fef50_weighted(age, height_cm, sex)
        fef75_pred, fef75_lln, fef75_uln = fef75_weighted(age, height_cm, weight_kg, sex)

        results.append({
            'sex': sex,
            'height_cm': height_cm,
            'age': age,
            'weight_kg': weight_kg,
            'FVC_Pred': fvc_pred,
            'FVC_LLN': fvc_lln,
            'FVC_ULN': fvc_uln,
            'FEV1_Pred': fev1_pred,
            'FEV1_LLN': fev1_lln,
            'FEV1_ULN': fev1_uln,
            'FEV1_FVC_Pred': fev1_fvc_pred,
            'FEV1_FVC_LLN': fev1_fvc_lln,
            'FEV1_FVC_ULN': fev1_fvc_uln,
            'PEFR_Pred': pefr_pred,
            'PEFR_LLN': pefr_lln,
            'PEFR_ULN': pefr_uln,
            'FEF25_75_Pred': fef25_75_pred,
            'FEF25_75_LLN': fef25_75_lln,
            'FEF25_75_ULN': fef25_75_uln,
            'FEF50_Pred': fef50_pred,
            'FEF50_LLN': fef50_lln,
            'FEF50_ULN': fef50_uln,
            'FEF75_Pred': fef75_pred,
            'FEF75_LLN': fef75_lln,
            'FEF75_ULN': fef75_uln
        })

    output_df = pd.DataFrame(results)
    try:
        output_df.to_csv(output_file_path, index=False)
        print(f"Results successfully saved to '{output_file_path}'")
    except Exception as e:
        print(f"Error writing output file: {e}")

if __name__ == "__main__":
    input_file = r"d:\Users\Tejaswini\Desktop\neurosyn\Indian\patients_india.csv"  # Name of your input Excel file
    output_file = 'india_parameters.csv'  # Name for your output Excel file
    process_lung_function_data(input_file, output_file)