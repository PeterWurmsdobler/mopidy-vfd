import logging
import queue
import threading
import time
from datetime import datetime

log = logging.getLogger(__name__)


class DisplayController(object):
    def __init__(self, status_queue, display) -> None:
        self.status_queue = status_queue
        self.display = display
        self._delay = 0.2
        self._thread = None

    def start(self):
        log.info("Display update loop starting ...")
        if self._thread is not None:
            return

        self._running = threading.Event()
        self._running.set()
        self._thread = threading.Thread(target=self._loop)
        self._thread.start()

    def stop(self):
        self._running.clear()
        self._thread.join()
        self._thread = None

    def _loop(self):
        log.info("Display update loop started")
        while self._running.is_set():
            timsteap = datetime.now()
            player_status = None
            try:
                player_status = self.status_queue.get(timeout=self._delay)
                self.status_queue.task_done()

            except queue.Empty:
                pass
            finally:
                self.display.update(timsteap, player_status)

            time.sleep(self._delay)
        log.info("Display update loop stopped")
