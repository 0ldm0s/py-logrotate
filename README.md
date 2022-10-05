# WHY HAVE THIS?
I use pm2 in my server, but `pm2-logrotate` consumption is so very huge.
So, I wrote this. For me, and anyone.
# HOW TO USE?
You can download this file in any where.(like wget, curl, etc...)
## WGET
```sh
wget https://raw.githubusercontent.com/0ldm0s/py-logrotate/master/logrotate.py
```
## COMMAND LINE
You need Python 3.x for this file. you can using `apt` or `dnf`, also `pyenv` etc.
```sh
pm2 start logrotate.py --name "py-logrotate" --time --interpreter=python --no-autorestart --cron "* * * * *"
```
## ecosystem
```javascript
    {
        name: "py-logrotate",
        cwd: "in your path",
        script: "logrotate.py",
        interpreter: "python",
        merge_logs: false,
        time: true,
        autorestart: false,
        cron_restart: "* * * * *"
    }
```
# THANK YOU
Thank you for use. :)