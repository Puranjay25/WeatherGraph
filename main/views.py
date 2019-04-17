from django.shortcuts import render
import requests
import pprint


def index(request):
	if request.method=="POST":
		api='https://api.openweathermap.org/data/2.5/forecast/hourly?q={}&appid=cf4d5bdc6f70e14a3bc9c5029d0b4bd0'
		city=request.POST.get("city")

		weather=requests.get(api.format(city)).json()

		temperature=[k['main']['temp'] for k in weather['list']]

		'''dates=[]
		for k in weather['list']:
			k1=k['dt_txt'].split(' ')
			k1=k1[0]
			k1=k1.replace('-','')
			dates.append(k1)'''

		dates=[k['dt'] for k in weather['list']]


		zipped=list(zip(dates,temperature))
		weather=list()

		for z in zipped:
			newdict=dict()
			newdict['date']=z[0]
			newdict['temperature']=z[1]
			weather.append(newdict)


		return render(request,"index.html",{"weather":weather})

	return render(request,"index.html")