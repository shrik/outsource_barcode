# requirements
python >=  3.6

# install 
pip install -r requirements.txt


# start
nohup python app.py 5051 > server.log &

# stop
ps aux | grep python | grep 5055

  '> ecs-user  806785  0.1  0.4 561356 31952 pts/2    Sl+  11:33   0:00 python app.py 5055'
  
kill 806785


# check process
ps aux | grep python | grep 5055
