#!/usr/bin/python3
#on same physical server
def total_share(str1, str2):
	f1 = open(str1, "rb")
	f2 = open(str2, "rb")
	a1 = f1.readlines()
	a2 = f2.readlines()
	len1 = len(a1)
	len2 = len(a2)
	count = 0
	print("No. of pages in ",str1,": " + str(len1))
	print("No. of pages in ",str2,": " + str(len2))

	all_pages = a1 + a2;

	count = len(set(all_pages));

	print("Common hashes: "+str(count)," MB")
	return len(a1)+len(a2)-count;

def final_usage(li):
	all_pages = []
	for str in li:
		f = open(str, "rb")
		all_pages = all_pages + f.readlines()

	return int(len(set(all_pages))/256);

def intervm_sharing(str1, str2):
	f1 = open(str1, "rb")
	f2 = open(str2, "rb")
	a1 = f1.readlines()
	a2 = f2.readlines()
	len1 = len(a1)
	len2 = len(a2)
	count = 0
	print("No. of pages in ",str1,": " + str(len1))
	print("No. of pages in ",str2,": " + str(len2))

	all_pages = set(a1) & set(a2);

	count = len(all_pages);
	print("Common hashes: "+str(count/256)," MB")
	return count;

#experiment
def printing_results():
    print("Idle sharing ", total_share("../memTraces/correctnessIdle/VM1.txt0", "../memTraces/correctnessIdle/VM2.txt0"))
    print("Loaded sharing ", total_share("../memTraces/correctnessLoaded/VM1.txt1", "../memTraces/correctnessLoaded/VM2.txt1"))

    print("Change percentage over period of time(2 min) in idleSystem, 2GB")
    all_files = []
    for i in range(3):
        all_files = all_files + ["../memTraces/idleSystem/VM1.txt"+str(i)]

    for i in range(2):
        f1 = open(all_files[i], "rb")
        f2 = open(all_files[i+1], "rb")
        a1 = f1.readlines()
        a2 = f2.readlines()
        change = 100*len(set(a1+a2) - (set(a1) & set(a2)))/len(a1)
        print("Change ", change, "%")

    print("Change percentage over period of time(2 min) in loaded system, 2GB")
    all_files = []
    for i in range(3):
        all_files = all_files + ["../memTraces/Trace1/VM1.txt"+str(i)]

    for i in range(2):
        f1 = open(all_files[i], "rb")
        f2 = open(all_files[i+1], "rb")
        a1 = f1.readlines()
        a2 = f2.readlines()
        change = 100*len(set(a1+a2) - (set(a1) & set(a2)))/len(a2)
        print("Change ", change, "%")