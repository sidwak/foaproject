import tkinter as tk
from tkinter import ttk
import random
import networkx as nx
import matplotlib.pyplot as plt

class JobMatchingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Job Matching App")

        self.jobs = []
        self.workers = []
        self.job_worker_edges = []
        self.graph = nx.DiGraph()
        self.graph.add_node('source')
        self.graph.add_node('sink')

        # Job Entry
        self.job_entry = tk.Entry(master, width=30)
        self.job_entry.grid(row=0, column=0, padx=5, pady=5)
        self.job_add_button = tk.Button(master, text="Add Job", command=self.add_job)
        self.job_add_button.grid(row=0, column=1, padx=5, pady=5)

        # Worker Entry
        self.worker_entry = tk.Entry(master, width=30)
        self.worker_entry.grid(row=1, column=0, padx=5, pady=5)
        self.worker_add_button = tk.Button(master, text="Add Worker", command=self.add_worker)
        self.worker_add_button.grid(row=1, column=1, padx=5, pady=5)

        # Jobs Listbox
        self.jobs_listbox = tk.Listbox(master, width=40, height=10, exportselection=False)
        self.jobs_listbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Workers Listbox
        self.workers_listbox = tk.Listbox(master, width=40, height=10, exportselection=False)
        self.workers_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # Job-Worker Edge Creation
        self.create_edge_button = tk.Button(master, text="Create Job-Worker Edge", command=self.create_edge)
        self.create_edge_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Job-Worker Edges Listbox
        self.job_worker_listbox = tk.Listbox(master, width=40, height=10)
        self.job_worker_listbox.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        # Run Algorithm Button
        self.run_algorithm_button = tk.Button(master, text="Run Algorithm", command=self.run_algorithm)
        self.run_algorithm_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        # Final Output Table
        self.output_table = ttk.Treeview(master, columns=("Job", "Worker"))
        self.output_table.heading("#0", text="ID")
        self.output_table.heading("Job", text="Job")
        self.output_table.heading("Worker", text="Worker")
        self.output_table.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    def add_job_worker_edge(self, job, worker, capacity):
        self.graph.add_edge(job, worker, capacity=capacity)

    def find_maximal_flow(self):
        self.flow_value, self.flow_dict = nx.maximum_flow(self.graph, 'source', 'sink')
        return self.flow_value, self.flow_dict
    
    def assign_jobs(self, jobs, workers, asign_dict):
        # for job in jobs:
        #     for worker in workers:
        #         if worker in self.graph.successors(job) and self.graph[job][worker]['capacity'] == 1:
        #  
        #            print(f"Assign {job} to {worker}")
        i = 0
        for job in jobs:
            for key in asign_dict[job]:
                if (asign_dict[job][key] == 1):
                    print(f"Assign {job} to {key}")
                    self.output_table.insert("", tk.END, text=i+1, values=(job, key))
                    break
        nx.draw_spectral(self.graph, with_labels = True)
        #nx.draw_circular
        #nx.draw_spring
        plt.savefig("filename4.png")

    def calalgo(self):
        self.flow_value, self.flow_dict = self.find_maximal_flow()
        print(self.flow_dict)
        print(self.flow_value)

    def print_final_output(self):
        for each in self.flow_dict:
            print(each, self.flow_dict[each])
            self.assign_jobs(self.jobs, self.workers, self.flow_dict)
    
    def add_job(self):
        job = self.job_entry.get()
        if job:
            self.jobs.append(job)
            self.add_job_worker_edge('source', job, 1)
            self.jobs_listbox.insert(tk.END, job)
            self.job_entry.delete(0, tk.END)

    def add_worker(self):
        worker = self.worker_entry.get()
        if worker:
            self.workers.append(worker)
            self.add_job_worker_edge(worker, 'sink', 1)
            self.workers_listbox.insert(tk.END, worker)
            self.worker_entry.delete(0, tk.END)

    def create_edge(self):
        selected_job = self.jobs_listbox.curselection()
        selected_worker = self.workers_listbox.curselection()
        if selected_job and selected_worker:
            job = self.jobs[int(selected_job[0])]
            worker = self.workers[int(selected_worker[0])]
            self.add_job_worker_edge(job, worker, 1)
            self.job_worker_edges.append((job, worker))
            print("added edge",job,worker)
            self.job_worker_listbox.insert(tk.END, f"{job} - {worker}")

    def run_algorithm(self):
        # You can implement the maximal flow algorithm here
        # Populate the output table with the results
        self.calalgo()
        #self.print_final_output()
        self.assign_jobs(self.jobs, self.workers, self.flow_dict)
        #for i, (job, worker) in enumerate(self.job_worker_edges):
            #self.output_table.insert("", tk.END, text=i+1, values=(job, worker))

def main():
    root = tk.Tk()
    app = JobMatchingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
