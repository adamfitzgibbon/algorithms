import re

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def validate (field, value):
  if field == "byr":
    value = int(value)
    return value >= 1920 and value <= 2020
  if field == "iyr":
    value = int(value)
    return value >= 2010 and value <=2020
  if field == "eyr":
    value = int(value)
    return value >= 2020 and value <= 2030
  if field == "hgt":
    cmPos = value.find("cm")
    if cmPos != -1:
      value = int(value[:cmPos])
      return value >= 150 and value <= 193
    inPos = value.find("in")
    if inPos != -1:
      value = int(value[:inPos])
      return value >= 59 and value <= 76
    return False
  if field =="hcl":
    return re.search("^#[0-9a-f]{6}$", value)
  if field == "ecl":
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
  if field == "pid":
    return re.search("^[0-9]{9}$", value)
  return True

with open("4_input.txt", 'r') as f:
  valid_passports = 0
  visited_fields = required_fields.copy()
  for line in f:
    if len(line.rstrip()) == 0:
      if len(visited_fields) == 0:
        valid_passports += 1
      visited_fields = required_fields.copy()
      continue
    for entries in line.split(" "):
      field, value = entries.split(":")
      if field in visited_fields and validate(field.rstrip(), value.rstrip()):
        visited_fields.remove(field)
  if len(visited_fields) == 0:
    valid_passports += 1
  print(valid_passports)