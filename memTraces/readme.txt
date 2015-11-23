idleSytem
folder contains the memory traces for ubuntu 14.04 with 2GB ram

kernelBuild
folder contains the memory traces for ubuntu 14.04 with 2GB ram during kernel build


correctnessIdle
2 VMs running Ubuntu 14.04 each with 2 GB memory with idle system
Pages actually shared:
sudo cat /sys/kernel/mm/ksm/pages_shared = 44196
Sharing predicted by the hashes match:
33783
227581 and 273124 hashes


correctnessLoaded
2 VMs running Ubuntu 14.04 each with 2 GB memroy with firefox(also with youtube video), libre office and nautilius open
Predicted : 69377
Actual Sharing : 77491
439687 and 451991 respectively

Trace1
the memory traces of loaded vm (32 bit ubuntu 14.04, 2GB ram, per 2 min)

Trace2
the memory traces of loaded vm (32 bit ubuntu 14.04, 2GB ram, per 2 min)

Trace3
the memory traces of loaded vm (64 bit ubuntu 14.04, 1GB ram, per 2 min)

Trace4
the memory traces of loaded vm (64 bit ubuntu 14.04, 1GB ram, per 2 min)
