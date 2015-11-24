#!/usr/bin/python3

from analyse import final_usage
from analyse import intervm_sharing
##########Input
file_name = ["../memTraces/Trace3/VM1.txt0",
			 "../memTraces/kernelBuild/VM1.txt1",
			 "../memTraces/Trace3/VM1.txt2",
			 "../memTraces/Trace1/VM1.txt0",
			 "../memTraces/Trace4/VM1.txt0"]

vm_size = [1024, 2048, 1024, 2048, 1024]
binsize = [3072, 3072, 3072]
initial_map = [0,0,1,1,2]
###########Input ends

n = len(vm_size);

share = [[0 for x in range(n)] for x in range(n)];
for i in range(n):
	for j in range(i+1,n):
		share[i][j] = intervm_sharing(file_name[i], file_name[j]);

bins_no = len(binsize);

maxi = 0;
max_posx = 0;
max_posy = 0;

matched = [-1 for x in range(n)];

for i in range(n):
	for j in range(n):
		if (maxi < share[i][j]):
			maxi = share[i][j];
			max_posx = i;
			max_posy = j;


binsize[0] = binsize[0] - vm_size[max_posx];
binsize[0] = binsize[0] - vm_size[max_posy];
matched[max_posx] = 0;
matched[max_posy] = 0;
#print(matched);
best = 0;
best_pos = -1;
curr_bin = 0;
count = 0;

i = 0;
while i < n-2:
	best = 0;
	count = 0;
	best_pos = -1;
	for j in range(n):
		temp = 0;
		count = 0;
		if (matched[j] != -1):
			continue;
		for k in range(n):
			if (matched[k] == curr_bin):
				temp = temp + share[j][k]/(count+1.0);
				count = count + 1;
		if (temp >= best):
			best = temp;
			best_pos = j;

	if (binsize[curr_bin] > vm_size[best_pos]):
		print(best_pos);
		matched[best_pos] = curr_bin
	else:
		if (curr_bin == bins_no):
			print("No more available machines\n");
		else:
			curr_bin = curr_bin + 1;
			i = i - 1;

			maxi = 0;
			max_posx = -1;
			max_posy = -1;

			for k in range(n):
				if (matched[k] != -1):
					continue;
				for l in range(n):
					if (k == l):
						continue;
					if (matched[l] != -1):
						continue;
					if (maxi < share[k][l]):
						maxi = share[k][l];
						max_posx = k;
						max_posy = l;

			if (max_posy == -1):
				for k in range(n):
					if (matched[k] == -1):
						matched[k] = curr_bin;
				break;

			binsize[curr_bin] = binsize[curr_bin] - vm_size[max_posx];
			binsize[curr_bin] = binsize[curr_bin] - vm_size[max_posy];
			matched[max_posx] = curr_bin;
			matched[max_posy] = curr_bin;
			i = i + 1;
	i = i+1;

for i in range(n):
	print ('VM #',i,' goes to machine', matched[i])

initial_mem = 0;
final_mem = 0;

for i in range(bins_no):
	str_set = [];
	for j in range(n):
		if (initial_map[j] == i):
			str_set = str_set + [file_name[j]];
	temp = final_usage(str_set)
	initial_mem = initial_mem + temp;
	print('Memory usage before colocation on physical machine #',i," is ",temp,"MB")

for i in range(bins_no):
	str_set = [];
	for j in range(n):
		if (matched[j] == i):
			str_set = str_set + [file_name[j]];
	temp = final_usage(str_set)
	final_mem = final_mem + temp;
	print('Memory usage after colocation on physical machine #',i," is ",temp,"MB")

print('Initial usage was',initial_mem,"MB");
print('After colocation memory usage was',final_mem,"MB");
print('Memory saved is ',initial_mem - final_mem ,"MB")