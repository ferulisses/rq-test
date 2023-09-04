# rq-test
Setup:

```
python -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
chmod +x run.sh
```

Tests:
```
./run.sh run  # will create a job
./run.sh worker  # will run a worker
./run.sh results  # will get results
```

