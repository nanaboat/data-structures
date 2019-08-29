import sched
import time

def hello():
    print('hello')
    print(time.time())

def periodic(scheduler, interval, action, events_queue, actionargs=()):
    if len(events_queue) < 3:
        event_id = scheduler.enter(interval, 1, periodic, (scheduler, interval, action, events_queue, actionargs))
        action(*actionargs)
        events_queue.append(event_id)
        

    #print(scheduler.queue)


if __name__ == '__main__':
    s = sched.scheduler()
    events = []
    periodic(s, 10, hello, events)
    #print(time.time())
    s.run()
    print(events)    