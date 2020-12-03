""" An implementation of merge sort in Python """

def merge_sort(l):
  length = len(l)
  if length == 1 or length == 0:
    return l

  mid = int(length/2)
  left = merge_sort(l[:mid])
  right = merge_sort(l[mid:])
  return merge(left, right)

def merge(l1, l2):
  merged_list = []
  while len(l1) > 0 and len(l2) > 0:
    if l1[0] <= l2[0]:
      merged_list.append(l1.pop(0))
    else:
      merged_list.append(l2.pop(0))
  return merged_list + l1 + l2

print(merge_sort([5,3,8,7,1,2,-1]))