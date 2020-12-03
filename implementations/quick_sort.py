""" An implementation of quick sort in Python """

def quick_sort(l):
  if len(l) == 1 or len(l) == 0:
    return l

  pivot = l.pop()
  less = [x for x in l if x <= pivot]
  greater = [x for x in l if x > pivot]

  return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([5,3,8,7,1,2,-1]))