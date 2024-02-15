import random
import networkx as nx
import matplotlib.pylab as plt

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
        nx.draw_spectral(self.graph, with_labels = True)
        #nx.draw_circular
        #nx.draw_spring
        plt.savefig("filename2.png")


if __name__ == "__main__":
    job_matching = JobMatching()

    jobs = ['job1', 'job2', 'job3']
    workers = ['worker1', 'worker2', 'worker3']

    job_matching.graph.add_node('source')
    job_matching.graph.add_node('sink')

    for job in jobs:
        job_matching.add_job_worker_edge('source', job, 1)
    for worker in workers:
        job_matching.add_job_worker_edge(worker, 'sink', 1)


    job_matching.add_job_worker_edge('job1', 'worker1', 1)
    job_matching.add_job_worker_edge('job1', 'worker2', 1)
    job_matching.add_job_worker_edge('job2', 'worker2', 1)
    job_matching.add_job_worker_edge('job2', 'worker3', 1)
    job_matching.add_job_worker_edge('job3', 'worker1', 1)
    job_matching.add_job_worker_edge('job3', 'worker3', 1)

    flow_value, flow_dict = job_matching.find_maximal_flow()
    print("Maximal Flow:", flow_value)
    print("Number of Workers:", len(worker))
    print("Number of Jobs:",len(jobs))

    #print(flow_dict)
    for each in flow_dict:
        print(each, flow_dict[each])
    print("\n")

    job_matching.assign_jobs(jobs, workers, flow_dict)
