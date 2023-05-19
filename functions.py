
import pandas as pd

class FCFS:

    ################################################################
    def exit_time(dizionario : dict): 
        # cumulative execution times

        times = []
        
        for n,i in enumerate(dizionario.keys()):
            
            if n == 0:
                times.append(dizionario[i][1])
        
            else:
                times.append(times[n-1] + dizionario[i][1])
        
        new_diz = {v[0]:(*v[1], x) for v, x in zip(dizionario.items(), times)}
        
        return new_diz
    

    def turn_around_times(dizionario : dict):   #
        
        a_list = []
        
        for i in dizionario.keys():

            desired = dizionario[i][2] - dizionario[i][0]
            # difference between Exit time and Arrival of the processes

            if desired < 0: 
                desired = dizionario[i][1]
            # if negative there is no queue ahead, so TAT = Burst_time
            # perche WT = TAT - Burst_time deve essere  0
            # not sure 

            a_list.append(desired)

        new_diz = {v[0]:(*v[1], x) for v, x in zip(dizionario.items(), a_list)}

        return new_diz


    def waiting_times(dizionario : dict):
        
        a_list = []
        
        for i in dizionario.keys():
            
            wt = dizionario[i][3]-dizionario[i][1]
            # difference between turn around time and burst time

            a_list.append(wt)
        
        new_diz = {v[0]:(*v[1], x) for v, x in zip(dizionario.items(), a_list)}
        
        return new_diz

    
    def Scheduling(queue : list, µ = 0.1):   # queue is list of dict

        arrival_time_tasks = [int(queue[i]["Arrival_Time"]) for i in range(len(queue))]
        running_time_tasks = [(queue[i]["CPU"]/ µ)*1000 for i in range(len(queue))]      # from seconds to milliseconds

        dict_values = list(zip(arrival_time_tasks, running_time_tasks))

        d = {int(queue[key]["Job_ID"]): dict_values[key] for key in range(len(queue))}
        d = dict(sorted(d.items(), key=lambda item: item[1])) # sort by time arrival (not sure if needed)
        # KEY = job_id --> VALUES = Arrival_Time, Burst_time

        my_list = [x[0] for x in d.values()]
        time_deltas = [my_list[i]-my_list[i-1] if i !=0 else 0 for i in reversed(range(len(my_list)))][::-1]
        new_d = {v[0]:(new,v[1][1]) for v, new in zip(d.items(), time_deltas)}
        # KEY = job_id --> VALUES = Time_delta, Burst_time

        results = FCFS.exit_time(new_d)
        results = FCFS.turn_around_times(results)
        results = FCFS.waiting_times(results)
        # KEY = job_id --> VALUES = Time_delta, Burst_time, Exit_time, Turn_around_time, Waiting_time

        df = pd.DataFrame.from_dict(results, orient='index').reset_index()
        df.columns = ["Job_id", "Time_deltas", "execution_time", "exit_time", "turn_around", "waiting"]


        return df









