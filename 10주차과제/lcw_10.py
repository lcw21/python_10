#과제25
keys = input("키를 입력하세요: ").split()
values = list(map(int, input("값을 입력하세요: ").split()))

d = dict(zip(keys, values))

d.pop('alpha', None)
d.pop('delta', None)

print(d)

#과제26
park = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
print("english:", park['english'])
print("science:", park['science'])

#과제27
kim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
x = dict.fromkeys(kim, 100)
print(x)

#과제28
lee = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

if 'english' in lee:
  lee.pop('english')
print(lee)

#과제29
lim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

for i in lim.items():
  print(i, end='')
  
#과제30
choi = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
scores = {k: v for k, v in choi.items() if v >= 90}
print(list(scores.keys()))

#과제31
yoo = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

avg = sum(yoo.values()) / len(yoo)
print("평균: ", avg)