from hashlib import md5

with open("input.txt", 'r') as f:
  input = f.readline()
  i = 0
  while True:
    result = md5((input + str(i)).encode())
    if result.hexdigest()[:6] == "000000":
      print(i)
      break
    i += 1