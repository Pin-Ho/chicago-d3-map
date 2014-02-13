#!/usr/bin/python

import json


json_data = open("cta_json.json")
data = json.load(json_data)

data_features = data['features']

for i in range(data_features.__len__()):
	if data_features[i]['geometry']['coordinates'].__len__() == 2:
		data_features[i]['geometry']['coordinates'][0]=float(data_features[i]['geometry']['coordinates'][0])
		data_features[i]['geometry']['coordinates'][1]=float(data_features[i]['geometry']['coordinates'][1])
	else:
		iter = 0
		while iter < data_features[i]['geometry']['coordinates'].__len__():
			data_features[i]['geometry']['coordinates'][iter][0]=float(data_features[i]['geometry']['coordinates'][iter][0])
			data_features[i]['geometry']['coordinates'][iter][1]=float(data_features[i]['geometry']['coordinates'][iter][1])
			iter +=1

print json.dumps(data)

	#for j in data_features[count]['geometry']['coordinates']:
		#count_0 = 0
		#data_features[count]['geometry']['coordinates'][0]= float(data_features[count]['geometry']['coordinates'][0])
		#count_0+=1
		#print count_0
	#if data_features[i]['geometry']['coordinates'].__len__() < 3:
			#count_0 = 0
			#data_features[count]['geometry']['coordinates'][count_0]= float(data_features[count]['geometry']['coordinates'][count_0])
			#count_0 +=1
	#	print "We changed something here!"
	#else:
#		print "too long"

		

		
