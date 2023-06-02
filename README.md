# Networking for Big-Data
Homework two for the [**Networking for Big Data and Laboratory**](""ttps://web.uniroma1.it/netlab/networking-big-data-and-laboratory") course at Sapienza University of Rome

## Challenge #2 Outline:

Consider a *computational cluster* composed of a **job dispatcher device** and **$N$ servers**,\
each one equipped with its own processing and memory resources.\
The goal is to develop a *dispatching algorithm* and *scheduling algorithms* to achieve the best mean job response time.

**Baseline algorithms:**\
`Least Work Left` dispatching (LWL) and `First Come First Served` scheduling for servers (FCFS)

### Assumptions:

- Each server has the same processing power **µ**, expressed in GNCU.\
Hence, the service time of a task is $x = CPU/µ$.
- Each server has a memory amount of 1 GNMU.
- Pre-emption is allowed as well as server sharing, if deemed useful.
- It is not allowed to kill a job or a task, i.e., all tasks must be worked out eventually.
- The dispatcher and servers have knowledge of the exact service time of a task upon its arrival.
- Delay and loss are negligible for message exchange among the dispatcher and the servers.
- Each running task is assigned the memory space it requires as long as it is running.\
Swapping a task from running to standby and back requires negligible time.
- At any given time, the sum of all assigned memory workspaces to running tasks on a given server shall not exceed the overall memory of that server.

**Constraints** : &emsp; **µ** = 0.1 &nbsp;, &emsp; **N** = 64

### Metrics:

Metrics used to evaluate the performance of the computational cluster:

- `Job Response Time (R):` Job response time is defined as the time elapsed from the arrival of the first task of a job until all tasks belonging to that job have been fully served. The mean job response time ($\bar{R}$) is obtained by averaging the response times of all jobs.

- `Job Slowdown (R):` Job slowdown is calculated as the ratio of the response time of a job to the sum of the service times of all tasks belonging to that job. The mean job slowdown ($\bar{S}$) is obtained by averaging the slowdown values of all jobs.

- `Utilization Coefficient (ρk):` The utilization coefficient of server k (ρk) represents the fraction of time that server k is busy serving tasks. The overall mean utilization coefficient (ρ) is calculated as the average of ρk values for all servers: ρ = (ρ1 + ρ2 + ... + ρN) / N.

- `Messaging Load (L):` Messaging load refers to the number of messages exchanged between the dispatcher and servers for a given task dispatching. The mean message load ($\bar{L}$) is obtained by averaging the message load values of all tasks.

---------------------------------------------------------

### Dataset:

The workload for the computational cluster is described by a dataset obtained from measurements on a production data center of Google, which is publicly available and can be downloaded from [here](https://github.com/MertYILDIZ19/Google_cluster_usage_traces_v3_Cell_a).

The dataset is a five-column table in CSV format, comprising $2,329,133$ rows.\
Each column represents the following information:

1. `Job_ID:` An integer number representing the identifier of a job.
2. `Task_ID:` An integer number between $0$ and n<sub>j</sub> representing the identifier of tasks belonging to job j.
3. `tₐ:` Arrival time of a task measured in microseconds.
4. `CPU:` Running time in seconds required to run the task on a Google Normalized Computing Unit (GNCU).
5. `Memory:` Amount of memory required to run the task, expressed in Google Normalized Memory Unit (GNMU).

---------------------------------------------------------
