import os
import _thread
import time
import threading






# Set user input as domain to fuzz
domain = input("Domain: ")
num_thread = int(input("Number of threads: "))
print("fuzzing top 1000 subdomains for "+domain+"...")


# Create file to save successfully tested subdomains
# Open bitquark top 100 subdomains and read each line into a list
#
# Updates are regularly made to this list on bitquark github
# https://github.com/bitquark/dnspop
results = open("working_subdomains.txt", "w")
results.write("Working Subdomains for "+domain+"\n")
results.close()

global subdomains
with open("bitquark_20160227_subdomains_popular_1000") as subdomains:
    subdomains = subdomains.readlines()

# Scrub new line character and parse to string
for i in range(len(subdomains)):
    subdomains[i] = str(subdomains[i])
    subdomains[i] = subdomains[i].replace('\n', '')



# NEW LEIT HACKER CODE BRO
#def runWget(subDomains, domain):

class thread_wget(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        # Add loop into this function to keep popping through the stack
        global subdomains
        while(len(subdomains) > 0):
            subDomain = subdomains.pop()
            cmd = "wget -q -O - -U demo http://"+subDomain+"."+domain+"/df.txt --header \"Host: domainfronter.pages.dev\""
            res = os.system(cmd)
            if res != "":
                print(subDomain+" fronted successfully\n" + cmd + "\n\n")
                #results.write(subDomain+"\n")
            else:
                print(subDomain+" not fronted!!!!!!!!!!!" + "\n")


for i in range(0, num_thread):
    thread_wget("fuck_you" + str(i)).start()




# Future additions:
#   -Create a "domainfronter.pages.dev" variant on each of the popular CDNs
#   -User chooses from list of CDNs and program choose corresponding Host header
