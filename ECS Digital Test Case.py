import sqlite3
import re
from glob 		import glob
from os.path 	import join

def check_File_Version():
	"""Check the SQL script version numbers in folder"""
	filename = glob(join(expanduser('~'), '*', re.search("((\d{3}).*?createtable.sql)")
	fileVersionNumber = filename(0)
	return fileVersionNumber

# Check the SQLLite version table for current version number
def check_DB_Version():
	"""Check the SQLLite version table for current version number"""
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	dbVersionNumber = c.execute("SELECT * FROM VERSION_TABLE ORDER BY NAME ASC LIMIT 1;")
	dbVersionNumber = re.search("(\d{3}).*?createtable.sql", dbVersionNumber)
	conn.close()
	return dbVersionNumber	

# Compare the file version number against the Database version number
if check_File_Version() == check_DB_Version():
	print("Database is up to date.")

elif check_File_Version() > check_DB_Version():
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	
	scriptFile = open(check_File_Version())
	script = scriptFile.read()
	scriptFile.close()
	
	cursor.executescript(script)
	conn.commit()
	conn.close()