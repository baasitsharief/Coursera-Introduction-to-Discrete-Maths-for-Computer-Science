def PascalsTriangle(C, N):   #C is a dictionary object, N is the height

  for n in range(N):
    C[n,0] = 1
    C[n,n] = 1
    
    for k in range(1,n):
      C[n,k] = C[n-1,k-1]+C[n-1,k]
  return C
