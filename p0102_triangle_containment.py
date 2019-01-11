  # 107: triangle containment (CORRECT! 15% difficulty!!!!!)
  #logic: if the origin is within, lines to the origin from each vertex separate triangle into three parts
  # which sum to the overall triangle area. Using the fact that Area triangle = 1/2||AB x AC||, we can see these
  # sub triangles are made up of the vectors AO, BO, CO where O is the origin. They then have areas 1/2||AO x BO|| etc
  with(open('p102_triangles.txt')) as inputFile:
      count = 0
      for line in inputFile:
          line = line.strip()
          points = line.split(",")
          A = [int(points[0]), int(points[1])]
          B = [int(points[2]), int(points[3])]
          C = [int(points[4]), int(points[5])]
          # in two dimensions, cross product is easy ||[a b 0] x [c d 0]|| = absolute(ad - bc)
  
          vectAB = np.subtract(B,A)
          vectAC = np.subtract(C,A)
  
          #works!
          trueArea = 0.5*np.absolute(vectAB[0]*vectAC[1] - vectAB[1]*vectAC[0])
  
          # AO x BO
          subArea1 = 0.5*np.absolute(A[0]*B[1] -A[1]*B[0])
  
          # AO x CO
          subArea2 = 0.5*np.absolute(A[0]*C[1] - A[1]*C[0])
  
          # BO x CO
          subArea3 = 0.5*np.absolute(B[0]*C[1] - B[1]*C[0])
  
          if trueArea == subArea1 + subArea2 + subArea3: count += 1
  print (count)

