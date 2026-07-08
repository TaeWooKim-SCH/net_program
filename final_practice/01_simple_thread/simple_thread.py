import threading

def prtSquare(num):
    print("Square: {}".format(num ** 2))

def prtCube(num):
    print("Cube: {}".format(num ** 3))

# 쉼표가 있어야 튜플로 인식
t1 = threading.Thread(target=prtSquare, args=(10, ))
t2 = threading.Thread(target=prtCube, args=(10, ))

# 각 스레드 시작 -> prtSquare와 prtCube가 병렬로 실행
t1.start()
t2.start()

# 스레드 종료 대기 -> 해당 스레드가 끝날 때까지 메인 스레드를 기다리게 함
# - 두 스레드가 모두 완료된 뒤에야 프로그램이 다음으로 넘어가거나 종료됨
t1.join()
t2.join()

print('Done!')