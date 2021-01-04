import requests
import json

if __name__ =="__main__":
  print("Getting Files from DB.")

  r = requests.get('https://cs-revise.leroysalih.vercel.app/api/challenge/1', data = {'main':'#Written from gitpod'})
  obj = json.loads(r.text)
  

  f = open("./main.py", "w")
  f.write(obj['main'])
  f.close()

  f = open("./test.py", "w")
  f.write(obj['test'])
  f.close()

  print("Files generated")
