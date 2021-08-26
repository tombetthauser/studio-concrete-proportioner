import os

adjustments_dict = {
  "overall": 1.44,
  "sand": -0.15,
  "flow_control": .15
}

conversion_table = {
  "water": 27.5,
  "concrete": 110,
  "flow_control": 1,
  "sand": 25,
  "pigment": 2 
}

input_dict = {
 "total_vol_ml": None
}

output_dict = {}

output_ml_dict = {
  "water": None,
  "concrete": None,
  "flow_control": None,
  "sand": None,
  "pigment": None
}

os.system("clear")
print("----- CONCRETE PROPORTIONER -----\n")
input_dict["total_vol_ml"] = int(input("Enter total desired volume in milliliters: "))

proportion_total = 0

for k in conversion_table:
  proportion_total += conversion_table[k]

for k in conversion_table:
  conversion_table[k] = conversion_table[k] / proportion_total
  output_dict[k] = round(input_dict["total_vol_ml"] * conversion_table[k] * adjustments_dict["overall"], 2)
  if k in adjustments_dict:
    multiplyer = adjustments_dict[k]
    if multiplyer < 0:
      multiplyer = 1 - (-1 * multiplyer)
    else:
      multiplyer = 1 + multiplyer
    output_dict[k] = round(output_dict[k] * multiplyer,  2)

print("\n\n--- CURRENT PROPORTIONS ---\n")

percent_total = 0

for k in conversion_table:
  print(k, round((conversion_table[k] * 100), 2), "%")
  percent_total += conversion_table[k]

print("\ntotal: ", percent_total * 100, "%")

print("\n\n--- OUTPUT MEASUREMENTS ---\n")

measurements_total = 0

for k in output_dict:
  print(k, output_dict[k], "(ml)")
  measurements_total += output_dict[k]

print("\ntotal: ", round(measurements_total, 2), "(ml)")

print("\n--- END ---\n\n")
