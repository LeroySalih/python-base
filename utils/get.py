import requests
import json
import os
import sys
from colour import red, green



if __name__ =="__main__":

  if os.path.isfile('main.py'):

    cont = input(f'{red("main.py")} already exists.  This command will overwrite the file.  Continue (y)? ')

    if not( cont == 'y'):
      print(red("Stopping"))
      sys.exit(0)

  id = os.environ.get('CHALLENGE_ID')
  title = os.environ.get("CHALLENGE_TITLE")
  email = os.environ.get("EMAIL")

  print(f"Getting Files for Challenge ID {id} from DB.")
  print("")

  r = requests.get(f"https://cs-revise.leroysalih.vercel.app/api/challenge/{id}")
  obj = json.loads(r.text)
  

  f = open("./main.py", "w")
  f.write(obj['main'])
  f.close()

  f = open("./tests/maintestengine.py", "w")
  f.write(obj['test'])
  f.close()

  f = open("./README.md", "w")
  f.write(obj['README'])
  f.close()

  print(green("Files generated"))
