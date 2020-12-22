import regex as re
memo = {}
def get_memo_or_compute(rules, ruleNum):
  if ruleNum in memo:
    return memo[ruleNum]
  else:
    result = compute_valid_results(rules, ruleNum)
    memo[ruleNum] = result
    return result

def compute_valid_results(rules, ruleNum):
  if rules[ruleNum] in ["a", "b"]:
    return rules[ruleNum]
  rule = rules[ruleNum].split(" | ")
  if len(rule) == 2:
    leftRule, rightRule = rule
    leftPointers, rightPointers = leftRule.split(" "), rightRule.split(" ")
    leftLists = [get_memo_or_compute(rules, pointer) for pointer in leftPointers]
    rightLists = [get_memo_or_compute(rules, pointer) for pointer in rightPointers]
    return f"(({''.join(leftLists)})|({''.join(rightLists)}))"
  else:
    pointers = rule[0].split(" ")
    lists = [get_memo_or_compute(rules, pointer) for pointer in pointers]
    if ruleNum == "8":
      lists.append("+")
    if ruleNum == "11":
      lists.insert(0, "(?<rec>(")
      lists.insert(2, ")(?&rec)?(")
      lists.append("))")
    return "".join(lists)
with open("input.txt", 'r') as f:
  lines = [x.rstrip() for x in f.readlines()]
  rules = {}
  inputs = []
  isInputs = False
  for line in lines:
    if not line:
      isInputs = True
    if isInputs:
      inputs.append(line)
    else:
      label, rule = line.split(": ")
      rules[label] = rule.replace('"', '')
  # 0: 8 11
  # rules["8"] = "42 | 42 8"
  # rules["11"] = "42 31 | 42 11 31"
  # validResults = set(compute_valid_results(rules, "0"))
  s = compute_valid_results(rules, "0")
  expr = re.compile(s)
  print(expr)
  counter = 0
  for input in inputs:
    if expr.fullmatch(input):
      counter += 1
  print(counter)