# schedule by linux cmd crontab



* list crontab

```
# crontab -l
```

* add a daily scheduler

```
# crontab -e
```

Then add line as below

```
0 2 * * * /bin/sh backup.sh
```

This means backup db every 02:00am daily





