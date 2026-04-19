from collections import Counter

def main():

    s = input()
    if not s:
        return
        
    # 각 문자의 등장 횟수 세기
    counts = Counter(s).values()
    
    # 등장 횟수가 모두 짝수인지, 모두 홀수인지 판별
    all_even = all(count % 2 == 0 for count in counts)
    all_odd = all(count % 2 == 1 for count in counts)
    
    # 조건에 맞게 결과 출력
    if all_even:
        print(0)
    elif all_odd:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    main()