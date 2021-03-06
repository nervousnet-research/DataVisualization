# The code generates the output in a file called timestamps.txt
# The output has the following format :
#		UUID | max_timestamp max_date | min_timestamp min_date
# The input comes from the local mysql database. The database is called
# CCC and the table is called SENSOR_b.
# The code was written by Siddhartha for
#              ------------------------------------------------------
#                          Computational Social Science
#              Department of Humanities, Social and Political Sciences
#                         Prof. Dirk Helbing (ETH, Zurich)
#                               Clausiusstrasse 50
#                                  CLU Building
#                            8092 Zürich, Switzerland
#              ------------------------------------------------------

import MySQLdb
import time
import numpy
import math
import datetime

# to find the maximum and minimum timpestamps of all the phone id's.
# this gives us the duration the phone was sending the data.This info
# is usually important for any temporal analysis.

def __getTimestamps():
	# connect to the local SQL database where the data is.
	# connect to the database (host,username,password,database)
	db = MySQLdb.connect("localhost","root","27feb1988","CCC");
	print "Successful Connection....";

	# get the node cursor
	cn = db.cursor();

	# find the maximum and minimum timestamps of each UUID and
	# write in a file.
	query0 = "select HEX(UUID),max(RecordTIme),min(RecordTime) from SENSOR_b GROUP BY UUID";
	cn.execute(query0);

	fileName = 'timestamps.txt';
	f = open(fileName,'w');

	for x in cn.fetchall():
		max_date = datetime.datetime.fromtimestamp(int(x[1]/1000)).strftime('%Y-%m-%d %H:%M:%S');
		min_date = datetime.datetime.fromtimestamp(int(x[2]/1000)).strftime('%Y-%m-%d %H:%M:%S');

		print >> f,'%s | %s %s | %s %s' % (x[0],x[1],max_date,x[2],min_date);

if __name__ == "__main__":
	__getTimestamps();
