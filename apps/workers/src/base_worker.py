from .logging import configure_logging
from .redis_connector import RedisConnector

class BaseWorker:
    def __init__(self):
        configure_logging()
        self.redis = RedisConnector()

    def startup(self):
        import logging
        logging.info("Worker starting…")
        logging.info(f"Redis: {self.redis.connect()}")

    def run(self):
        self.startup()
        self.process()

    def process(self):
        raise NotImplementedError("Workers must implement process().")
