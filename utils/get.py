import requests
import json
import os
if __name__ =="__main__":
  challengeId = os.environ.get('CHALLENGE_ID')
  print(f"Getting Files for Challenge ID {challengeId} from DB.")
  print("")

  

  r = requests.get(f"https://cs-revise.leroysalih.vercel.app/api/challenge/{challengeId}")
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

  print("Files generated")
