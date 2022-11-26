def arithmetic_arranger(problems, solve=False):

  if len(problems) > 5:
    return "Error: Too many problems."

  firstNums = []
  secondNums = []
  operators = []

  for problem in problems:
    firstNums.append(problem.split()[0])
    secondNums.append(problem.split()[2])
    operators.append(problem.split()[1])

  for num in firstNums:
    if len(num) > 4:
      return "Error: Numbers cannot be more than four digits."

  for num in secondNums:
    if len(num) > 4:
      return "Error: Numbers cannot be more than four digits."

  for operator in operators:
    if (operator != "+") and (operator != "-"):
      return "Error: Operator must be '+' or '-'."
      
  try:
    for num in firstNums:
      int(num)
    for num in secondNums:
      int(num)
  except:
    return "Error: Numbers must only contain digits."

  topRow=[]
  bottomRow=[]
  dashes=[]
  answers=[]

  print(firstNums, secondNums, operators)
  
  for i in range(len(firstNums)):
    if len(firstNums[i]) > len(secondNums[i]):
      topRow.append(" "*2 + firstNums[i])
    else:
      topRow.append(" "*(len(secondNums[i]) - len(firstNums[i]) + 2) + firstNums[i])
    
  print(topRow)

  for i in range(len(secondNums)):
    if len(secondNums[i]) > len(firstNums[i]):
      bottomRow.append(operators[i] + " "+ secondNums[i])
    else:
      bottomRow.append(operators[i]+" "+" "*(len(firstNums[i])-len(secondNums[i]))+secondNums[i])

    dashes.append("-"*len(bottomRow[i]))

  print(bottomRow)
  print(dashes)

  if solve:
    for i in range(len(firstNums)):
      if operators[i] == "+":
        ans = str(int(firstNums[i])+int(secondNums[i]))
        spaces = len(dashes[i]) - len(str(ans))
        answers.append(" "*spaces+ans)
      else:
        ans=str(int(firstNums[i])-int(secondNums[i]))
        spaces = len(dashes[i]) - len(str(ans))
        answers.append(" "*spaces+ans)

    print(answers)
    return '    '.join(topRow)+"\n"+'    '.join(bottomRow)+"\n"+'    '.join(dashes)+"\n"+'    '.join(answers)
  else:
    return '    '.join(topRow)+"\n"+'    '.join(bottomRow)+"\n"+'    '.join(dashes)
    
    