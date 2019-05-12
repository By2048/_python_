import asyncio

@asyncio.coroutine
def begin():
    print("Starting to wait.")
    asyncio.get_event_loop().call_later(10, end)

def end():
    print("completed")

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(begin())
        loop.run_forever()
    except KeyboardInterrupt:
        print("Goodbye!")