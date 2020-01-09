k8.py#!/usr/bin/python3
import os

print("Welcome to the console K8 app")

pods = os.popen("kubectl get pods --template '{{range .items}}{{.metadata.name}}{{\",\"}}{{end}}'").read().split(",")
podsLen = len(pods) - 1 # 0 counts as one.

for i in range(podsLen):
    print("{}: {}".format(i+1, pods[i]))

selection = input("Select a pod or 0 to exit: ")

if selection.isnumeric() and podsLen >= int(selection) > 0:
    print("Connecting to {} pod".format(pods[int(selection)-1]))
    os.system("kubectl exec -it {} /bin/bash".format(pods[int(selection)-1]))
elif int(selection) == 0:
    exit()
else:
    print("Invalid selection")
