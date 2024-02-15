import random
import networkx as nx
import matplotlib.pyplot as plt

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
        nx.draw_spectral(self.graph, with_labels = True)
        #nx.draw_circular
        #nx.draw_spring
        plt.savefig("filename.png")


if __name__ == "__main__":
    job_matching = JobMatching()
    
    jobs = ['Software Engineer', 'Data Analyst', 'Graphic Designer', 'Project Manager', 'Marketing Specialist',
             'Customer Support Representative', 'Accountant', 'Human Resources Manager', 'Content Writer',
               'Sales Representative', 'Network Administrator', 'UI/UX Designer']
    workers = ['John', 'Emma', 'Michael', 'Sophia', 'James', 'Olivia', 'William', 'Isabella', 'Liam', 'Ava', 'Benjamin',
                'Mia', 'Linus', 'Luke', 'Josh', 'Taylor', 'Ariana', 'Drake', 'Liljay', 'Mrbeast', 'Felix', 'Lana', 'Miley']

    job_matching.graph.add_node('source')
    job_matching.graph.add_node('sink')

    for job in jobs:
        if (job == "Software Engineer"):
            job_matching.add_job_worker_edge('source', job, 3)
        elif (job == "Data Analyst"):
            job_matching.add_job_worker_edge('source', job, 2)
        elif (job == "Graphic Designer"):
            job_matching.add_job_worker_edge('source', job, 2)
        elif (job == "Customer Support Representative"):
            job_matching.add_job_worker_edge('source', job, 5)
        elif (job == "Accountant"):
            job_matching.add_job_worker_edge('source', job, 2)
        elif (job == "Sales Representative"):
            job_matching.add_job_worker_edge('source', job, 3)
        else:
            job_matching.add_job_worker_edge('source', job, 1)
    for worker in workers:
        job_matching.add_job_worker_edge(worker, 'sink', 1)

    #Skills
    job_matching.add_job_worker_edge('Software Engineer', 'John', 1)
    job_matching.add_job_worker_edge('Software Engineer', 'Emma', 1)
    job_matching.add_job_worker_edge('Software Engineer', 'Linus', 1)
    job_matching.add_job_worker_edge('Data Analyst', 'Emma', 1)
    job_matching.add_job_worker_edge('Data Analyst', 'Michael', 1)
    job_matching.add_job_worker_edge('Data Analyst', 'Mrbeast', 1)
    job_matching.add_job_worker_edge('Graphic Designer', 'Michael', 1)
    job_matching.add_job_worker_edge('Graphic Designer', 'Sophia', 1)
    job_matching.add_job_worker_edge('Graphic Designer', 'Luke', 1)
    job_matching.add_job_worker_edge('Project Manager', 'Sophia', 1)
    job_matching.add_job_worker_edge('Project Manager', 'Lana', 1)
    job_matching.add_job_worker_edge('Project Manager', 'James', 1)
    job_matching.add_job_worker_edge('Marketing Specialist', 'James', 1)
    job_matching.add_job_worker_edge('Marketing Specialist', 'Olivia', 1)
    job_matching.add_job_worker_edge('Marketing Specialist', 'Miley', 1)
    job_matching.add_job_worker_edge('Customer Support Representative', 'Olivia', 1)
    job_matching.add_job_worker_edge('Customer Support Representative', 'William', 1)
    job_matching.add_job_worker_edge('Customer Support Representative', 'Josh', 1)
    job_matching.add_job_worker_edge('Customer Support Representative', 'Taylor', 1)
    job_matching.add_job_worker_edge('Customer Support Representative', 'Mrbeast', 1)
    job_matching.add_job_worker_edge('Customer Support Representative', 'Miley', 1)
    job_matching.add_job_worker_edge('Customer Support Representative', 'Felix', 1)
    job_matching.add_job_worker_edge('Customer Support Representative', 'Taylor', 1)
    job_matching.add_job_worker_edge('Accountant', 'William', 1)
    job_matching.add_job_worker_edge('Accountant', 'Isabella', 1)
    job_matching.add_job_worker_edge('Accountant', 'Ariana', 1)
    job_matching.add_job_worker_edge('Human Resources Manager', 'Isabella', 1)
    job_matching.add_job_worker_edge('Human Resources Manager', 'Liam', 1)
    job_matching.add_job_worker_edge('Human Resources Manager', 'Felix', 1)
    job_matching.add_job_worker_edge('Content Writer', 'Liam', 1)
    job_matching.add_job_worker_edge('Content Writer', 'Ava', 1)
    job_matching.add_job_worker_edge('Sales Representative', 'Ava', 1)
    job_matching.add_job_worker_edge('Sales Representative', 'Benjamin', 1)
    job_matching.add_job_worker_edge('Sales Representative', 'Drake', 1)
    job_matching.add_job_worker_edge('Sales Representative', 'Liljay', 1)
    job_matching.add_job_worker_edge('Network Administrator', 'Benjamin', 1)
    job_matching.add_job_worker_edge('Network Administrator', 'Mia', 1)
    job_matching.add_job_worker_edge('UI/UX Designer', 'Mia', 1)
    job_matching.add_job_worker_edge('UI/UX Designer', 'John', 1)


    flow_value, flow_dict = job_matching.find_maximal_flow()
    print("Maximal Flow:", flow_value)
    print("Number of Workers:", len(worker))
    print("Number of Jobs:",len(jobs))

    #print(flow_dict)
    for each in flow_dict:
        print(each, flow_dict[each])

    job_matching.assign_jobs(jobs, workers, flow_dict)
