import subprocess
command = "ssh -i /home/ubuntu/.node-red/certs/sora.pem ubuntu@ec2-18-198-100-246.eu-central-1.compute.amazonaws.com <<-'SSHEND' " + """
df /
free -m
iostat -c
SSHEND
"""
result=str( subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read())
#print(result.replace("\\n","---"))
output = (result.replace("\\n","---"))
out = output.split("---")
i = 0 
cpu = 0 
payload = []
for rows in out:
#    print(rows)
    if rows:
        line = (rows.split())
        if line[0] == "/dev/root":
            payload.append(line[1]) # Disk size in Kb
            payload.append(line[4].replace("%","")) # Percetage of disk space used 
        if line[0] == "Mem:":
            payload.append(line[1]) # Total
            payload.append(line[2]) # Used
            payload.append(line[3]) # Free
        if cpu  == 1:
            payload.append(line[0]) # %user
            payload.append(line[1]) # %nice
            payload.append(line[2]) # %system
            payload.append(line[3]) # %iowait
            payload.append(line[4]) # %steal
            payload.append(line[5]) # %idle
            cpu = 0
        if line[0] == "avg-cpu:":
            cpu = 1
#       print(str(line[0]) + ": cpu : " +str(cpu))
#    print("=o==========================")
    i = i + 1

payload_s = ","
print(payload_s.join(payload))

#avg-cpu:  %user   %nice %system %iowait  %steal   %idle
#           0.27    0.00    0.06    0.03    0.01   99.62
