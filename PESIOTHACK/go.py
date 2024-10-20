import time
import random
import data_pb2
from golain import GolainClient
#import aqi_pb2

shadow = data_pb2.Shadow()
#aqi = aqi_pb2.aqi()
#aqi.pm25 = 123

device = GolainClient(None)

device.connect()
print("64646")
device.client.loop_start()

def shadowCallback(data):
  print(f'received shadow data: {data}')
  newShadow = data_pb2.Shadow()
  newShadow.ParseFromString(data)
  print(newShadow)

device.setShadowCallback(shadowCallback)
device._publish(f'/{device.root_topic}/{device.device_name}/device-shadow/u', shadow.SerializeToString())

while(1):
  device.publishData('S', shadow.SerializeToString())
  time.sleep(1)