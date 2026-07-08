import asyncio, time

async def get_user(name):
    print('사용자 {!r} 정보 조회중...'.format(name))
    await asyncio.sleep(1) # time.sleep 을 쓰면 동기로 진행됨, await 쓰면 오류남
    print('사용자 {!r} 정보 조회 완료!'.format(name))

async def main():
    start = time.time()
    await asyncio.gather(get_user('Kim'),
        get_user('Lee'),
        get_user('Park'),
        get_user('Choi'))
    end = time.time()
    print(f'총 소요시간: {end - start}')

asyncio.run(main())