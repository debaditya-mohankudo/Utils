import asyncio, httpx, time


start = time.time()
print(start)

CONCURRENT_REQUESTS = 30 # ~ parallel requests 
TOTAL_REQUESTS = 100
 
cc_auth = {'X-DC-DEVKEY': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}
end_point = 'https://localhost.xxxxxx.com/services/v2/order/277670380'



async def request_api(i):
    async with httpx.AsyncClient() as client:
        print(f"sending:: {i}  {time.time()}")
        return await client.post(end_point, headers=cc_auth)

async def producer(queue, i):
    r = await request_api(i)
    await queue.put((r, i))
 
async def consumer(queue):
    while True:
        #print(queue.qsize())
        try:
            result, i = await queue.get()
            print(f"received ::{i}  {time.time()}")
        except Exception as exc:
            print('generated an exception: %s' % ( exc))
        
        # process the token received from a producer
        queue.task_done()
        #print(f"consumed {result.json()}")
 
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
    #print('---- done producing')
 
    # wait for the remaining tasks to be processed
    await queue.join()
    end_time = time.time()

    print(f"Time taken:: {(end_time - start_time)}s")
 
    # cancel the consumers, which are now idle
    for c in consumers:
        c.cancel()

if __name__ == "__main__":
    asyncio.run(main())