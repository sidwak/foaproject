import random
import networkx as nx

class JobMatching:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_job_worker_edge(self, job, worker, capacity):
        self.graph.add_edge(job, worker, capacity=capacity)

    def find_maximal_flow(self):
        flow_value, flow_dict = nx.maximum_flow(self.graph, 'source', 'sink')
        return flow_value, flow_dict

    def assign_jobs(self, jobs, workers, asign_dict):
        # for job in jobs:
        #     for worker in workers:
        #         if worker in self.graph.successors(job) and self.graph[job][worker]['capacity'] == 1:
        #             print(f"Assign {job} to {worker}")
        for job in jobs:
            for key in asign_dict[job]:
                if (asign_dict[job][key] == 1):
                    print(f"Assign {job} to {key}")
                    break

if __name__ == "__main__":
    job_matching = JobMatching()

    jobs = ['Software Engineer', 'Data Analyst', 'Graphic Designer', 'Project Manager', 'Marketing Specialist', 'Customer Support Representative', 'Accountant', 'Human Resources Manager', 'Content Writer', 'Sales Representative', 'Network Administrator', 'UI/UX Designer']
    workers = ['John', 'Emma', 'Michael', 'Sophia', 'James', 'Olivia', 'William', 'Isabella', 'Liam', 'Ava', 'Benjamin', 'Mia']

    for job in jobs:
        job_matching.add_job_worker_edge('source', job, 1)
    for worker in workers:
        job_matching.add_job_worker_edge(worker, 'sink', 1)

    random.shuffle(workers)

    workjob = []
    for job in jobs:
        random.shuffle(workers)
        for worker in workers:
            if random.random() < 0.5: 
                job_matching.add_job_worker_edge(job, worker, 1)
                workjob.append({worker: job})


    flow_value, flow_dict = job_matching.find_maximal_flow()
    for wkjb in workjob:
        print(wkjb)

    print("Number of Workers:", len(worker))
    print("Number of Jobs:",len(jobs))

    #print(flow_dict)
    for each in flow_dict:
        print(each, flow_dict[each])
    print("\n")
    print("\nMaximal Flow:", flow_value)
  
    job_matching.assign_jobs(jobs, workers, flow_dict)
