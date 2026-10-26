from device_limit import load_counts, predict_limit_dates

for device_id, date in predict_limit_dates(load_counts()).items():
    print(device_id, "reaches the limit on", date)
