import asyncio, httpx, time
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

start = time.time()
print(start)

CONCURRENT_REQUESTS = 50 # ~ parallel requests 
TOTAL_REQUESTS = 200

LOG = dict()
 
# cc_auth = {'X-DC-DEVKEY': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}
# end_point = 'https://localhost.xxxxxxxxxx.com/services/v2/order/certificate/277670380'

end_point = 'http://localhost:8000/items/1'

async def request_api(i):
    async with httpx.AsyncClient() as client:
        r = await client.get(end_point)
        return r

async def producer(queue: asyncio.Queue, i):
    r = await request_api(i)
    # LOG[time.time()] = f"Pushing into queue:: {i}"
    await queue.put((r, i))
 
async def consumer(queue: asyncio.Queue):
    while True:
        try:
            result, i = await queue.get()
            #LOG[time.time()] = f'DEBUG: queue size is now {queue.qsize()}'
            LOG[time.time()] = f"received:: {i}  with http status code:: {result.status_code} time taken:: {result.elapsed.microseconds // 1000} ms"
        except Exception as exc:
            LOG[f'{i} generated an exception: {exc}']
        
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

    # cancel the consumers, which are now idle
    for c in consumers:
        c.cancel()

    for k, v in sorted(LOG.items()):
        print(f'{k} -> {v}')

    print('-' * 20)
    print(f"Time taken:: {(end_time - start_time)}s for {TOTAL_REQUESTS} requests")
    print('-' * 20)

if __name__ == "__main__":
    asyncio.run(main())
    