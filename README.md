과제25
dict(zip(keys, values)) <br> d.pop('alpha', None) zip()과 dict()을 이용해 사용자 입력 기반의 딕셔너리를 생성하고, pop() 메소드로 alpha와 delta 키-값 쌍을 안전하게 제거하는 방법을 실습했습니다.

과제26
park['english'] | 딕셔너리에서 키(Key)를 사용하여 'english', 'science' 과목의 값(Value)에 직접 접근하여 출력하는 기본 접근 방식을 구현했습니다.

과제27
dict.fromkeys(kim, 100) dict.fromkeys() 메소드를 사용하여 기존 딕셔너리 `kim`의 모든 키를 가져와, 값을 100으로 통일한 새로운 딕셔너리를 생성했습니다.

과제28
if 'english' in lee: <br> lee.pop('english') in  연산자로 키의 존재 여부를 확인한 후, pop()을 이용해 'english' 키와 값을 조건부로 제거하는 로직을 구현했습니다.

과제29
for i in lim.items(): items() 메소드를 활용하여 딕셔너리 `lim`의 모든 (키, 값) 쌍(튜플)을 순회하고 출력했습니다.

과제30
{k: v for k, v in choi.items() if v >= 90}  딕셔너리 컴프리헨션을 사용하여 딕셔너리 `choi`에서 90점 이상인 항목만 필터링하여 새로운 딕셔너리를 만들고, 해당 과목명(키)을 출력했습니다.

과제31
sum(yoo.values()) / len(yoo) values() 메소드로 값만 추출하고, 파이썬 내장 함수 sum()과 len()을 이용하여 딕셔너리에 저장된 점수들의 산술 평균을 계산했습니다.