# keeping score for a baseball game with strange rules.

# List of strings "ops" where "ops[i]" is the "ith" operation must apply to the record and is one of the following:
# "An integer x" - Record a new score of x.
# "+" - Record a new score equal to the sum of the previous two scores, it is guaranteed there will always be at least two previous scores.
# "D" - Record a new score that is the double of the previous score, it is guaranteed there will always be a previous score.
# "C" - Invalidate the previous score, removing it from the record, it is guaranteed there will always be a previous score.

# At the beginning of the game, start with an empty record and return the "sum" of all the scores in the record:
# Example:
# Input: ops = ["5","2","C","D","+"]
# Output: 30

# constraint 1: 1 <= ops.length <= 1000:
# constraint 2: ops[i] is "C" , "D", "+" , or a string represeinting an integer in the range [-3 * 104, 3 * 104]
# constraint 3: for operation "C" and "D" be at least one previous score on the record
# constraint 4: for operation "+" be at least two previous scores on the record

def calPoints(ops) -> int:
  """ 
  :type ops: List[str] - List of operations
  :rtype: int - Sum of scores after performing all operations
  """
  result = None
  # constraint 1: 1 <= ops.length <= 1000:
  if len(ops) >= 1000 or len(ops) < 1:
    return result
  stack_ops = []
  for i in range(len(ops)):
    # constraint 3: for operation "C" and "D" be at least one previous score on the record:
    if ops[i] == "C":
      if len(stack_ops) < 1:
        return result
      stack_ops.pop()
    elif ops[i] == "D":
      if len(stack_ops) < 1:
        return result
      stack_ops.append(stack_ops[-1] * 2)
    # constraint 4: for operation "+" be at least two previous scores on the record:
    elif ops[i] == "+":
      if len(stack_ops) < 2:
        return result
      stack_ops.append(stack_ops[-1] + stack_ops[-2])
    else:
      # ops[i] is in the range [-3 * 104, 3 * 104]:
      if int(ops[i]) < -3*104 or int(ops[i]) > 3*104:
        return result
      stack_ops.append(int(ops[i]))
  result = sum(stack_ops)
  return result
  
# ops = ["5","2","C","D","+"]
ops = ["5","-2","4","C","D","9","+","+"]
# ops = ["1"]
print(calPoints(ops))

# if __name__ == "__main__":
#   line = input()
#   ops = line.strip().split()
  
#   print(calPoints(ops))
