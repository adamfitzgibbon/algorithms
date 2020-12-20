import re
memo = {}
def get_memo_or_compute(rules, ruleNum):
  if ruleNum in memo:
    return memo[ruleNum]
  else:
    result = compute_valid_results(rules, ruleNum)
    memo[ruleNum] = result
    return result

def get_pairs(list1, list2):
  return [a+b for a in list1 for b in list2]

def compute_valid_results(rules, ruleNum):
  if rules[ruleNum] in ["a", "b"]:
    return rules[ruleNum]
  rule = rules[ruleNum].split(" | ")
  if len(rule) == 2:
    leftRule, rightRule = rule
    leftPointers, rightPointers = leftRule.split(" "), rightRule.split(" ")
    if len(leftPointers) > 1:
      list1, list2  = [get_memo_or_compute(rules, pointer) for pointer in leftPointers]
      leftResults = get_pairs(list1, list2)
    else: 
      leftResults = get_memo_or_compute(rules, leftPointers[0])
    if len(rightPointers) == 2:
      list1, list2 = [get_memo_or_compute(rules, pointer) for pointer in rightPointers]
      rightResults = get_pairs(list1, list2)
    elif len(leftPointers) == 3:
      list1, list2, list3  = [get_memo_or_compute(rules, pointer) for pointer in rightPointers]
      rightResults = [a+b+c for a in list1 for b in list2 for c in list3] 
    else:
      rightResults = get_memo_or_compute(rules, rightPointers[0])
    return leftResults + rightResults
  else:
    pointers = rule[0].split(" ")
    lists = [get_memo_or_compute(rules, pointer) for pointer in pointers]
    if len(lists) == 3:
      list1, list2, list3 = lists
      return [a+b+c for a in list1 for b in list2 for c in list3]
    elif len(lists) == 1:
      return lists[0]
    else:
      list1, list2 = lists
      return get_pairs(list1, list2)

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
  validResults = set(compute_valid_results(rules, "0"))
  counter = 0
  for input in inputs:
    if input in validResults:
      counter += 1
  print(counter)
