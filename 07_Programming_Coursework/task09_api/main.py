import requests
import json

def main():
  adrese_tyrion = "https://api.gameofthronesquotes.xyz/v1/author/tyrion/3"
  adrese_jon = "https://api.gameofthronesquotes.xyz/v1/author/jon/2"
  adrese_random = "https://api.gameofthronesquotes.xyz/v1/random/1"  


  lapas_atbilde1 = requests.get(adrese_tyrion)
  lapas_atbilde2 = requests.get(adrese_jon)
  lapas_atbilde3 = requests.get(adrese_random)


  if lapas_atbilde1.status_code == 200:
      dati_1 = json.loads(lapas_atbilde1.content)
   
  for cite_nr in range(len(dati_1)):
      print("'" + dati_1[cite_nr]["sentence"] + "'") 
      print("\t" + "--" + " " + dati_1[cite_nr]["character"]["name"] + "\n")

  if lapas_atbilde2.status_code == 200:
      dati_2 = json.loads(lapas_atbilde2.content)
  
  for quote_nr in range(len(dati_2)):
   
      print("'" + dati_2[quote_nr]["sentence"] + "'") 
      print("\t" + "--" + " " + dati_2[quote_nr]["character"]["name"] + "\n")

  if lapas_atbilde3.status_code == 200:
      dati_3 = json.loads(lapas_atbilde3.content)
      print("'" + dati_3["sentence"] + "'") 
      print("\t" + "--" + " " + dati_3["character"]["name"])

if __name__ == "__main__":
  main()