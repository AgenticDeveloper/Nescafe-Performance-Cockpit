import numpy as np

def predict_cpd(site_row):
    channel_factor = {"Hotel": 0.12, "B&I": 0.10, "Retail": 0.08, "Cafe": 0.15}
    base = site_row["footfall"] * channel_factor.get(site_row["channel"], 0.10)
    penalty = 0.85 if site_row.get("competitor_50m", False) else 1.0
    cpd = max(10, base * penalty)
    conf = int(np.clip(50 + (site_row["footfall"] / 10), 60, 95))
    return int(round(cpd)), conf

def fit_score(pred_cpd, machine_row):
    util = np.clip(pred_cpd / machine_row["capacity_cpd"], 0, 1)
    score = (1 - abs(util - 0.88)) * 100
    return int(np.clip(score, 0, 100)), float(util)

def roi_percent(pred_cpd, machine_row):
    cups = pred_cpd * 30
    gross = cups * machine_row["margin_per_cup"]
    opex = machine_row["opex_month"]
    amort = machine_row["capex"] / 24.0
    roi = (gross - (opex + amort)) / max(1.0, (opex + amort))
    return round(roi * 100, 1)

def next_best_actions(cpd_expected, cpd_actual, uptime_pct):
    gap = cpd_expected - cpd_actual
    actions = []
    if uptime_pct < 0.93:
        actions.append({"action": "Trigger service visit", "reason": "Low uptime", "expected_uplift": int(gap * 0.6)})
    if cpd_actual < cpd_expected and uptime_pct >= 0.93:
        actions.append({"action": "Run promo", "reason": "Demand shortfall", "expected_uplift": int(gap * 0.4)})
    if gap > 20:
        actions.append({"action": "Relocate or swap machine", "reason": "Large persistent gap", "expected_uplift": int(gap * 0.8)})
    return actions
