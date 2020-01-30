import requests
import json

url = "http://27.96.134.231:3389"
dic = {
    'Req': 'F',
    'Joint': '5',
    'Data': '10 20 30,40 50 60',
    'Time': '12:34:56'
}
header = {'Content-Type': 'application/json; charset=utf-8'} #이거 안해주면 개고생임 무적권 추가해주자 그래야 Body의 내용을 이해함
data = json.dumps(dic, indent=4) #json으로 변환해주는 부분
print(data)
recvd = requests.post(url, headers=header, data=data)  #POST는 데이터 전달 시 json형식으로 변환 해줘야함
print(recvd.text) #응답을 출력함  -> json으로 응답이 옴  200은 정상응답
recvd= recvd.json() #딕셔너리 타입으로 변환
resData = recvd['Response'] #딕셔너리의 Response의 데이터에 접근
print(resData)


