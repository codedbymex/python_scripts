#!/usr/bin/python
# compare two csv files and print the result using zenity.

import csv
import subprocess

with open('test1.csv', 'rb') as csvfile1:
	with open ("test2.csv", "rb") as csvfile2:
		reader1 = csv.reader(csvfile1)
		reader2 = csv.reader(csvfile2)
		rows1_col_a = [row for row in reader1]
		rows2 = [row for row in reader2]
		only_b = []
		for row in rows2:
			if row not in rows1_col_a:
				only_b.append(row)
	for i in only_b:
		subprocess.call(["zenity", "--info", "--text", ','.join(i)])
