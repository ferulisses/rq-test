
def test_return_dict(param = {}):
    return {
        "abc": "xyz"
    }

def job_load_success(job, connection, result, *args, **kwargs):
    args = job.args
    print(type(job))
    result = job.return_value()
    print(type(result))
    print(f'Job {job.id} Success, Result: {result}')

def job_load_failure(job, connection, type, value, traceback):
    print(f'Job {job.id} Failure: {job.exc_info}')

def job_load_stopped(job, connection):
    print(f'Job {job.id} Stopped')
