```
export PYTHONPATH=${PYTHONPATH}:${HOME}/Documents/api

coverage run --include=/home/akash/Documents/api/python/functions* -m pytest -v

coverage run --omit=/.local/,tests,/site-packages/ -m pytest -v

coverage report

coverage report -m

coverage html
```