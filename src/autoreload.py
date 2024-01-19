import asyncio
import subprocess

from hachiko.hachiko import AIOWatchdog, AIOEventHandler

WATCH_DIR = '.'
EXECUTABLE_FILE = 'main.py'


class MyEventHandler(AIOEventHandler):
    def __init__(self, process: subprocess.Popen, loop=None) -> None:
        super().__init__(loop)
        self.process = process
        self._method_map["opened"] = self.suppress

    async def on_modified(self, event) -> None:
        self.process.terminate()
        self.process = subprocess.Popen(['python', EXECUTABLE_FILE])

    async def suppress(self, *args, **kwargs) -> None:
        pass


class Watcher:
    def __init__(self, watcher: AIOWatchdog) -> None:
        self.watcher = watcher

    async def watch(self):
        self.watcher.start()
        try:
            while True:
                await asyncio.sleep(1)
        finally:
            self.watcher.stop()


async def main() -> None:
    process = subprocess.Popen(['python', EXECUTABLE_FILE])
    handler = MyEventHandler(process)
    watcher = Watcher(AIOWatchdog(WATCH_DIR, event_handler=handler))
    await watcher.watch()


if __name__ == '__main__':
    asyncio.run(main())
