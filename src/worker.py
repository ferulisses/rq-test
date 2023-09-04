from redis import Redis
import argparse
from rq import Worker, Queue, Connection
import config


if __name__ == '__main__':
    redis_conn = Redis(config.REDIS_HOST, config.REDIS_PORT, config.REDIS_DB, config.REDIS_PASSWORD)
    listen_queue = ["test"]

    with Connection(redis_conn):
        worker = Worker(list(map(Queue, listen_queue)))
        worker.work()
