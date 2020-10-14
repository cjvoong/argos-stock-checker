import json, requests,time

class Item:
    def __init__(self,id,name):
        self.name=name
        self.id=id


url='https://www.argos.co.uk/stores/api/orchestrator/v0/locator/availability?origin=LS81LD&maxResults=10&maxDistance=50&save=pdp-ss%3A%2F&ssm=tru'
headers={'authority': 'www.argos.co.uk','x-newrelic-id': 'VQEPU15SARAGV1hVDgMBUVY=','user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML,     like Gecko) Chrome/83.0.4103.97 Safari/537.36','content-type': 'application/json','accept': '*/*','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.argos.co.uk/product/6014179?clickSR=slp:term:weights:8:39:1','accept-language': 'en-US,en;q=0.9'}

items = [Item('7923104','£39.99 bench'),Item('6084934','10kg plates'),Item('7603259','£54.99 bench'),Item('6014179','5kg plates'),Item('7603259','£69.99 bench')]

slackurl='[some hook url]'


try:
    startmsg='{\'text\':\'started looking for argos stock...\'}'
    #requests.post(slackurl,headers={'content-type':'application/json'},data=startmsg)
    for x in range(10000):
        try: 
            for item in items:
                print('looking for ' + item.name)
                r=requests.get(url + '&skuQty=' + item.id + '_1',headers=headers)
                y=json.loads(r.text)
                found=0
                for store in y["stores"]:
                    if (store["availability"][0]["quantityAvailable"] > 0):
                        payload='{\'text\':\'found some stock at of ' + item.name + ' at ' + store["storeinfo"]["legacy_name"] + '!\'}'
                        print(payload)
                        #print(requests.post(slackurl,headers={'content-type':'application/json'},data=payload))
                        found=1
                        break
                if (found==0):            
                    print('didn\'t find any stock of ' + item.name + ' :(')
        except:
            print("An error occurred")
        finally:
            print("trying again in 20 mins...")
            time.sleep(1200)
finally: 
    exitmsg='{\'text\':\'exiting script...\'}'
    #requests.post(slackurl,headers={'content-type':'application/json'},data=exitmsg)
    print("exiting script...")
