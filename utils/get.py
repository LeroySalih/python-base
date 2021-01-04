import requests
import json

if __name__ =="__main__":
  print("Getting Files from DB.")

  r = requests.get('https://cs-revise.leroysalih.vercel.app/api/challenge/1', data = {'main':'#Written from gitpod'})
  obj = json.loads(r.text)
  print(obj)
  print(obj['main'])
  print(obj['test'])

