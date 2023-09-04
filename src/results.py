from redis import Redis
from rq.job import Job
from rq import Worker, Queue, Connection, Callback
from src.funcs import test_return_dict, job_success, job_failure, job_stopped
import config


if __name__ == '__main__':
    redis_conn = Redis(config.REDIS_HOST, config.REDIS_PORT, config.REDIS_DB, config.REDIS_PASSWORD)
    q = Queue("test", connection=redis_conn, default_timeout=8, failure_ttl=600, is_async=config.USE_WORKER)

    for job_id in q.finished_job_registry.get_job_ids():
        job = Job.fetch(job_id, redis_conn)
        print(type(job))
        result = job.latest_result()
        print(type(result))
        print(f'Job {job.id} {result.type}, Result: {result.return_value}')
