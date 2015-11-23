#!/usr/bin/python3

def share_potential(str1, str2):
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
	return count;

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