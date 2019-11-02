from huey import crontab
from huey.contrib.djhuey import task, periodic_task

# 非同期タスク
@task()
def async_task(a, b):
    return a / b

# 定期実行タスク。5分に1回実行
@periodic_task(crontab(minute="*/5"))
def heartbeat():
    print("alive")

