required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

with open("input.txt", 'r') as f:
  valid_passports = 0
  visited_fields = required_fields.copy()
  for line in f:
    if len(line.rstrip()) == 0:
      if len(visited_fields) == 0:
        valid_passports += 1
      visited_fields = required_fields.copy()
      continue
    for entries in line.split(" "):
      field = entries.split(":")[0]
      if field in visited_fields:
        visited_fields.remove(field)
  if len(visited_fields) == 0:
    valid_passports += 1
  print(valid_passports)