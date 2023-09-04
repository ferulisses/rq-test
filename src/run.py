from redis import Redis
from rq import Worker, Queue, Connection, Callback
from src.funcs import test_return_dict, job_load_success, job_load_failure, job_load_stopped
import config



if __name__ == '__main__':
    redis_conn = Redis(config.REDIS_HOST, config.REDIS_PORT, config.REDIS_DB, config.REDIS_PASSWORD)
    q = Queue("test", connection=redis_conn, default_timeout=8, failure_ttl=600, is_async=config.USE_WORKER)

    test_return_dict()

    q.enqueue(test_return_dict, {},
                on_success=job_load_success, 
                on_failure=job_load_failure,
                on_stopped=job_load_stopped)

