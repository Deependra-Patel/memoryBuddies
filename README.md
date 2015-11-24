Framework for smart colocation of VMs in virtualized data centers.

###Introduction
❖ In a multi-server data center, opportunities for page
sharing may be lost because the VMs holding identical
pages are resident on different hosts.  
❖ We are trying to exploit Page Sharing for Smart Colocation
in Virtualized Data Centers.

###Approach
❖ Generate hash for all pages of all guest VMs  
❖ Send this data to a central control VM which compares it to
hash of various other VMs  
❖ Control server makes decisions of migration using a
greedy heuristic approach at various intervals  

###Implementation
❖ <b>Memory Tracer</b> A daemon runs on guest VM. It inserts a kernel module which we go through
all the pages of the memory of the VM to calculate 32 bit hash(Super Fast hash) of each page and
then write to the hash file. Removes the module. sends file to control server.  
❖ <b>Control Node</b> It listens to the incoming hash files and stores them by running a server. It
also analyses the hashes of various VMs for colocation. 

Our work is related to paper memory Buddies http://dl.acm.org/citation.cfm?id=1508299
Please read pdfs in Report/ folder for more information.

###Folder Information
❖ <b>guestEnd</b> Folder contains hash Daemon which uses kernel module to generate hash and send over to the server.
This daemon can be run in linux kernel 4.1* only.  
❖ <b>serverEnd</b> Folder contains code for server(server.py) as well as the heuristic(best_matching.py)  
❖ <b>memTraces</b> Contains various memory traces taken for analysis and correctness proving,
memTraces/readme.txt contains info about the traces

###--- HOW TO RUN ---
linux kernel 4.1* only. (eg. Ubuntu 14+)  
The hash files will be stored in folder serverEnd with names VM1.txt[x] format where x increases for every next version of hash.
eg. VM1.txt0, VM1.txt1, ...  
1. Copy serverEnd code to the server VM/machine,  
2. Start server "./server.py"  
3. Copy guestEnd code to the VM,  
4. Configure server ip in hashDaemon.py with port.  
5. Change sleepSeconds (Time interval between hash generation) if required,  
6. "make"  
7. "sudo ./hashDaemon.py"

To test colocation heuristic,    
In folder serverEnd   
"./best_matching.py"

