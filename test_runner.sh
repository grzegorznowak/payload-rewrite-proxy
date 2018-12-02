python src/PReP.py &
PID1=$!
python tests/echo.py &
PID2=$!
pytest --cov=src/

kill -9 $PID1
kill -9 $PID2
