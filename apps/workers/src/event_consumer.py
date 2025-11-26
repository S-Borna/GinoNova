import logging
from .base_worker import BaseWorker

class EventConsumer(BaseWorker):
    def process(self):
        logging.info("EventConsumer online (no events yet).")
