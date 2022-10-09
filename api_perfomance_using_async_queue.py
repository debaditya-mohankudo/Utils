import asyncio, httpx, time


start = time.time()
print(start)

CONCURRENT_REQUESTS = 100 # ~ parallel requests 
TOTAL_REQUESTS = 100
 
cc_auth = {'X-DC-DEVKEY': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}
end_point = 'https://localhost.xxxxxxxxxx.com/services/v2/order/certificate/277670380'

async def request_api(i):
    async with httpx.AsyncClient() as client:
        print(f"sending:: {i}  {time.time()}")
        return await client.get(end_point, headers=cc_auth)

async def producer(queue, i):
    r = await request_api(i)
    await queue.put((r, i))
 
async def consumer(queue):
    while True:
        try:
            result, i = await queue.get()
            print(f"received ::{i}  {time.time()} with http status code {result.status_code}")
        except Exception as exc:
            print('generated an exception: %s' % ( exc))
        
        queue.task_done()

async def main():
    queue = asyncio.Queue(maxsize=CONCURRENT_REQUESTS)
    start_time = time.time()

    # fire up the both producers and consumers
    producers = [asyncio.create_task(producer(queue, _))
                 for _ in range(TOTAL_REQUESTS)]
    consumers = [asyncio.create_task(consumer(queue))
                 for _ in range(CONCURRENT_REQUESTS)]
 
    # with both producers and consumers running, wait for
    # the producers to finish
    await asyncio.gather(*producers)
 
    # wait for the remaining tasks to be processed
    await queue.join()
    end_time = time.time()

    print(f"Time taken:: {(end_time - start_time)}s")
 
    # cancel the consumers, which are now idle
    for c in consumers:
        c.cancel()

if __name__ == "__main__":
    asyncio.run(main())