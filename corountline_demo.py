#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-30 20:00:09
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: 协程示例。
@ LastTime: 2019-07-30 20:33:03
'''

import random
import Queue
import time
from collections import namedtuple

DEPARTURE_INTERVAL = 5

Event = namedtuple('Event', 'time proc action')


def taxi_proc_coroutline(ident, trips, start_time=0):
    now = yield Event(start_time, ident, 'leave garage')
    for _ in range(trips):
        now = yield Event(start_time, ident, 'pick up a passenger')
        now = yield Event(start_time, ident, 'drop off a passenger')
        # time.sleep(random.randint(1, 5))

    now = yield Event(start_time, ident, 'going home')


class Simulator(object):

    def __init__(self, procs_map):
        self.events = Queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)

        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ****')
                break

            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('taxi: {}\t{}{}'.format(proc_id, '\t' * proc_id,
                                          previous_action))
            active_proc = self.procs[proc_id]
            next_time = sim_time + random.randint(1, 100)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))


if __name__ == "__main__":
    taxis = {
        0: taxi_proc_coroutline(ident=0, trips=2, start_time=0),
        1: taxi_proc_coroutline(ident=1, trips=4, start_time=5),
        2: taxi_proc_coroutline(ident=2, trips=6, start_time=10)
    }
    sim = Simulator(taxis)
    sim.run(10000)
