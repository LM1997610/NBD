
from numpy import array, argmin, inf
from pandas import DataFrame
from Scheduling import First_Come_First_Service

class Size_Int_Task_Ass:
 
    def __init__(self, N : int, starting : float):
        
        self.N = N
        self.clock = starting
        self.register = []
        self.servers = [First_Come_First_Service(id, scheduling="FCFS") for id in range(N)]

        print("\n Dispatcher →", self.__class__.__name__)

    def clock_update(self, new_time_from_task):
        self.clock = new_time_from_task
        
    def SITA_dispatch(self, task):
        
        pointed = int(task['cumsum'])
    
        if pointed == 0:
          wk = array([self.servers[i].work_load if i in [0, 62, 63] else inf for i in range(self.N)])
          pointed = argmin(wk)

                
        self.servers[pointed].add_to_queue(task)
    
    def Closing(self):

        active_queues = [k for k in range(64) if len(self.servers[k].queue)>0]
        t = sum([len(self.servers[i].queue) for i in active_queues])
        print("\n Closing {} active server queues: {} → {} tasks...".format(len(active_queues), active_queues, t), end = " ")

        for i in active_queues:
            this_queue = self.servers[i].queue
            q = this_queue.copy()
            for n,job in enumerate(q):
                service = job['service_time']
                self.register.append({'Job_ID' :job['id'].split('_')[0],
                                        'Task_ID' : job['id'].split('_')[1],
                                        'Arrived_at' : job['Arrival_Time'],
                                        'Completed_at' : job['Arrival_Time']+service})
                if  len(this_queue[1:]) > 1:
                    q[n+1]['service_time'] += service

                self.servers[i].delete_from_queue()

        print(" done ✓ \n")

        jobs = [dic['Job_ID'] for dic in self.register]
        task = [dic['Task_ID'] for dic in self.register]
        completion = [dic['Completed_at'] for dic in self.register]

        output = DataFrame({'Job':jobs, 'Task':task, 'Completion_Time':completion})

        return output
        
    def queue_manager(self, task):

        active_queues = [server for server in self.servers if len(server.queue)>0]
        if len(active_queues) != 0:
            for server in active_queues:
                queue = server.queue
                now = task['Arrival_Time']
                delta = now-self.clock
                while delta > 0 and len(queue) > 0:
                    active = queue[0]
                    if active['service_time'] - delta <= 0:
                        self.register.append({  'Job_ID' : active['id'].split('_')[0],
                                                'Task_ID' : active['id'].split('_')[1],
                                                'Arrived_at' : active['Arrival_Time'],
                                                'Completed_at' : now+active['service_time']-delta   })
                        server.delete_from_queue()
                        delta -= active['service_time']
                        queue = server.queue
                    else:
                        active['service_time'] -= delta
                        break

    def print_status(self):

        print("\n number of servers: {} → {} \n".format(self.N, type(self.servers[0]).__name__))
        print("\t status:", str([self.servers[i].status for i in range(63)][:20])[:-1]+" ...] \n")
        print("\t wk_load:", str([self.servers[i].work_load for i in range(63)][:20])[:-1]+" ...] \n")
        print("\t memory:", str([self.servers[i].memory for i in range(63)][:20])[:-1]+" ...] \n")
        print("\t queue:", *[self.servers[i].queue for i in range(63)][:20], "...\n")
            