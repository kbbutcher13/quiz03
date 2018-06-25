#Quiz 3:

def dot(vector01, vector02):
  '''
  Python finds the dot product of the two vectors by multiplying the first values in each vector (x1*x2), then it adds the product of the second values from each vector (y1*y2), then it adds the product of the third values from each vector (z1*z2). The sum of the three products (x1*x2 + y1*y2 + z1*z2 = dot product), gives the dot product of the two vectors. Considering, vector01=[x1,y1,z1] and vector02=[x2,y2,z2]
  '''
  #This checks to see if the vectors have the same dimensions:
  if len(vector01) != len(vector02):
    print("error")
    return None
  
  #Line 13-19 tells Python how to find the dot product:
  else:
    answer = 0
    #Here it is telling Python to take the values from vector01 and multiply them by the values of vector02, then it adds up the three products:
    for x in range(len(vector02)):
      answer += vector01[x] * vector02[x]
     #Repeat until the code is satisfied with "return":
    return answer


def vecSubtract(vector01, vector02):
  '''
  Python finds the difference of the two vectors by subtracting the first value of each vector, then placing the answer to in order (left to right). Then it does the same for the second and third values, until the code is satisfied with a result vector of the difference of the two vectors. So, vector01=[x1,x2,x3] and vector02=[y1,y2,y3], therefore, answer=[x1-y1,x2-y2,x3-y3]
  '''
  #This checks to see if the vectors have the same dimensions:
  if len(vector01) != len(vector02):
    print("error")
    return None
  else:
  #Line 32-38 Python solves for the difference of the vectors:
    answer = []
    for x in range(len(vector01)):
      #Here Python takes each difference and places them in order with "append": 
      dif = vector01[x] - vector02[x]  
      answer.append(dif)
      ##Repeats until the code is satisfied with "return":
    return answer


def scalarVecMulti(scalar, vector03):
  '''
  Python solves for the product of the scalar and vector by multiplying each value of the vector by the scalar value. As it multiplies each value of the vector by the scalar, the answers stay in order as they were originally placed in the vector. 
  '''
  #Line 46-52 tells python how to find the product:
  answer = []
  #Here it is stating to take the values from the vector and apply line 39:
  for z in vector03:
    #This is where python finds the product and puts the most recent answer at the end of the solution with "append":
    answer.append(scalar*z)
  #Repeat until the code is satisfied or the product is complete (by using "return"):
  return answer

def infNorm(vector04):
  '''
  Python solves for the infinity norm by finding the absolute value of the greatest value in the vector. It starts with the value 0, then goes through the vector and compares each value to the current greatest value. Once it checks every value in the vector, it should be left with the infinity norm or the absolute value of the largest integer in the vector. 
  '''
  #Python finds the infinity norm in line 59-66:
  #Here is where it starts with 0:
  answer = 0
  for x in range(len(vector04)):
    #Now it compares each value to the previous greatest value:
    if abs(vector04[x])>answer:
      answer = vector04[x]
  #Repeat until the code is satisfied with "return":
  return answer



def normalize(vector04):
  '''
  Python finds the normalized vector by dividing 1 by the infNorm, then multiplying that by the vector. This gives the vector a value of "1", which satifies the normalization of the vector.
  '''
  #Here it is stating not to proceed unless the infNorm is not zero:
  if infNorm == 0:
    return vector04[x]
  #Line 78-84 solves for normilzed vector:
  else:
    answer = []
    for x in range(len(vector04)):
      #This is where it solves the nomalize:
      normalize = 1/(infNorm(vector04)) * vector04[x]
      #Here is where it organizes the answer with "append":
      answer.append(normalize)
    return answer



vector01 = [10, 20, 30]
vector02 = [3, 6, 9]
scalar = 5
vector03 = [15, 20]
vector04 = [7, 13, 21]

#scalarInvalid = [15, 20]
#vector03Invalid = 5


print(dot(vector01, vector02))
print(vecSubtract(vector01, vector02))
print(scalarVecMulti(scalar, vector03))
print(infNorm(vector04))
print(normalize(vector04))
#print(scalarVecMulti(scalarInvalid, vector03Invalid))
