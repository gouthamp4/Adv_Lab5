import requests;
import json;

# Name: Potlacheruvu, Goutham Reddy
# BlazerId: GP4

apiUrl = "https://michaelgathara.com/api/python-challenge"

# requests are used to make a REST Http call using get and converting or parsing resulting
#  response to json using json()
apiResponseData = requests.get(apiUrl).json()

#print(type(apiResponseData))

for challenge in apiResponseData:
  problem = challenge['problem'].replace("?","")
  # The eval() function evaluates the string as a Python expression, in this case challenege dict problem
  # which can be Addition or Substraction etc. and converting it into Integer
  problemResult = int(eval(problem))
  print(f"problem {challenge['id']} => {problem}=  {problemResult}")

