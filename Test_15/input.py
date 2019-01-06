from influxdb import InfluxDBClient
import datetime
import time as t
from datetime import timezone

try:
    client = InfluxDBClient(host='127.0.0.1', port=8086, username='root', password='root', database='gis')
except:
    print("Influxdb Error")

text=["More then 100 died due to massive earthquake and 1000 were wounded.","16 dead and more then 20 found injured cause of the unexpected flood. The families of the deceased were granted some amount.","More the 200 men perished and an estimate of 400 were wounded when the cave collapsed while they were mining.","A huge number of men were killed in a train accident. The estimated count of the dead was 700.","3 men expired recently, who were struggling from the injuries of the train accident.","10 people went missing while going on a trip to Mount Everest. 2 of them were found dead and 15 injured due o massive avalaunch.","Need help for the rescue of 20 men stuck under the tunnel due to earthquake.","10 men struggled for their life while they were caught in a flood and got stuck under a bridge.","The rescue team provided help, food and other commodities to the victims of the flood.","Drought affected victims were estimated to be more then 500 and most of them were farmers."]
lat=22.57378518
long=88.41757695
timestamp=20180827173212
time=datetime.datetime.utcnow()
for i in range(len(text)):
	time=datetime.datetime.utcnow()
	data = [
	{
		"measurement": "kml2",
		"time": str(time),
		"fields": {
			"lat":str(lat),
			"long":str(long),
			"text":text[i],
			"timestamp":str(timestamp)
		}
	}
	]
	client.write_points(data)
