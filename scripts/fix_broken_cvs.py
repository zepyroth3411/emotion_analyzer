import csv

raw_path = "../data/raw_dataset.csv"
fixed_path = "../data/fixed_raw_dataset.csv"

with open(raw_path, "r", encoding="utf-8") as infile, open(fixed_path, "w", encoding="utf-8", newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for i, row in enumerate(reader, start=1):
        if len(row) == 2:
            writer.writerow(row)
        else:
            print(f"⚠️ Línea {i} descartada: {row}")