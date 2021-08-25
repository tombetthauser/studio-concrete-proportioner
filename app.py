import os

config_dict = {
  "adjustment_index": 1.44
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
input_dict["total_vol_ml"] = int(input("Enter total volume in millileters: "))

proportion_total = 0

for k in conversion_table:
  proportion_total += conversion_table[k]

for k in conversion_table:
  conversion_table[k] = conversion_table[k] / proportion_total
  output_dict[k] = round(input_dict["total_vol_ml"] * conversion_table[k] * config_dict["adjustment_index"], 2)

print("\n\n--- OUTPUT ---\n")

for k in output_dict:
  print(k, output_dict[k], "(ml)")

print("\n--- END ---\n\n")
