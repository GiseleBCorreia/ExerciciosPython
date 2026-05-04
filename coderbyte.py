def FirstFactorial(num):
  if num==0:
    return 1
  # code goes here
  return num * FirstFactorial(num-1)

# keep this function call here 
print(FirstFactorial(input()))