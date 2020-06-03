import os, io, sys, re, time, base64, json
import webbrowser, urllib.request
 
def main():
    "main function"
    url = "http://m.weather.com.cn/data/101010100.html"
    stdout=urllib.request.urlopen(url)
    weatherInfo= stdout.read().decode('utf-8')
    #print(weatherInfo)
    jsonData = json.loads(weatherInfo)


    szCity = jsonData["weatherinfo"]["city"]
    print("城市: ", szCity)
    szTemp = jsonData["weatherinfo"]["temp1"]
    print("温度: ", szTemp)
    szWeather1 = jsonData["weatherinfo"]["weather1"]
    print("天气情况: ",szWeather1)
    szCityid = jsonData["weatherinfo"]["cityid"]
    print("城市编码: ",szCityid)
   
if __name__ == '__main__':
    main()
