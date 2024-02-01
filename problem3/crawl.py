# -*- coding: UTF-8 -*-
import requests
import time
import pandas as pd
from const import startTimeStamp, base_url, params, headers

def listStats(shortMediaItems):
  print('{:>20} | {:>20} | {:>8} | {:>8} | {:>8} | {:>10} | {:>5} | {:<18}'.format('date', 'id', 'collect', 'comment', 'like', 'play', 'share', 'title'))
  print('-' * 120)
  for sm in shortMediaItems:
    print('{:>20} | {:>20} | {:>8} | {:>8} | {:>8} | {:>10} | {:>5} | {:<15}'.format( time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(sm['createTime'])), sm['id'], sm['stats']['collectCount'], sm['stats']['commentCount'], sm['stats']['diggCount'], sm['stats']['playCount'], sm['stats']['shareCount'], sm['desc'][:10]))

def crawlStats(startTimeStamp):
  response = requests.request("GET", base_url+params, headers=headers)
  data = response.json()
  shortMediaItems = []
  
  for item in data['itemList']:
    if item['createTime'] > startTimeStamp:
      shortMediaItems.append(item)
  
  print('-' * 100)
  print("Number of getting stats after", time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(startTimeStamp)), ": ", len(shortMediaItems))
  print('-' * 100)
  return shortMediaItems

def cleanData(shortMediaItems):
  processedItems = []

  for item in shortMediaItems:
    processedItem = {
        'id': item['id'],
        'createTime': item['createTime'],
        'collectCount': item['stats']['collectCount'],
        'commentCount': item['stats']['commentCount'],
        'diggCount': item['stats']['diggCount'],
        'playCount': item['stats']['playCount'],
        'shareCount': item['stats']['shareCount'],
        'desc': item['desc']
    }
    processedItems.append(processedItem)
    
  return processedItems

def exportCSV(processedItems):
  df = pd.DataFrame(item for item in processedItems)

  t = (int)(time.time())
  df.to_csv(f'data/{t}.csv', encoding = 'utf-8',index = False)
  print(f"\nSuccessfully export data to data/{t}.csv\n")

if __name__ == '__main__':
  shortMediaItems = crawlStats(startTimeStamp)
  listStats(shortMediaItems)
  processedItems = cleanData(shortMediaItems)
  exportCSV(processedItems)