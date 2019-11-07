x  = int(input())
print(x)

for c in "string":
    print(c)

for i in range(0, 5):
    print(i, i**2)

score = {
    '수학' : 80,
    '국어' : 90,
    '음악' : 100
}
total_score = sum(score.values())
print(total_score)
avg = total_score / len(score)
print(avg)

# 2. 반 퍙균 구하기

scroes = {
    "a" : {
        "수학" : 80,
        "국어" : 90,
        "음악" : 100
    },
    "b" : {
        "수학" : 70,
        "국어" : 99,
        "음악" : 95
    }
}

a_sum = sum(scroes["a"].values())
b_sum = sum(scroes["b"].values())

a_avg = sum(scroes["a"].values()) / len(scroes["a"])
b_avg = sum(scroes["b"].values()) / len(scroes["b"])

avg1 = (a_sum + b_sum) / len(scroes)
avg2 = (a_avg + b_avg) / 2
print(avg1)
print(avg2)

city = {
    "서울" : [-6, -10, 5],
    "대전" : [-3, -5 , 2],
    "광주" : [0, -2, 10],
    "부산" : [2, -2 , 9]
}


#도시별 최근 3일 온도 평균은?

avg4 = ((sum(city["서울"]) / len(city["서울"]))
 + (sum(city["대전"]) / len(city["대전"]))
 + (sum(city["광주"]) / len(city["광주"]))
 + (sum(city["부산"]) / len(city["부산"]))) /len(city)

for name , temp in city.items():
    avg_temp  = sum(temp) / len(temp)
    print(f'{name} : 평균 기온은 {avg_temp}입니다.')

print(avg4)

#서울은 영상 2도였던 적이 있나요?
#### A if 조건문 else B 삼항 연산자 조건이 참이면 A 거짓이면 B
print("있어요") if 2 in city["서울"] else print("없어요")




