import celery

@celery.task
def my_background_task(arg1, arg2):
    # какое то задание 
    return print("result")


task = my_background_task.delay(10, 20)

