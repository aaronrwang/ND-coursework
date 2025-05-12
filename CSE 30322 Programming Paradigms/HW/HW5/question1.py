def move_robot(n):
  d = [[0,1],[1,0],[0,-1],[-1,0]] # array for directions
  res = [(0,0)] # res array
  pos = [0,0] # where its currently at

  # loop till n
  for i in range(n):
    pos[0]+=(i+1)*d[i%4][0]
    pos[1]+=(i+1)*d[i%4][1]
    res.append((pos[0],pos[1]))
  return res