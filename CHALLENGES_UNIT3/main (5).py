def linearSearchProduct(productlist,targetproduct):
  indices = []

  for index,product in enumerate(productlist):
    if product == targetproduct:
      indices.append(index)

  return indices


products=["Sandals","shoes","Shoes","Boots","Sandals","Loafers","Sandals"]
target= "Sandals"
target2="Socks"
result=linearSearchProduct(products,target)
print(result)