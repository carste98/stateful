import psycopg2
import sys
import os
from dotenv import load_dotenv

# Check correct amount of args
if len (sys.argv) != 2 :
    print("Usage: checkVersion.py [IP]")
    sys.exit (1)

# load env
load_dotenv()
# connect to db
conn = psycopg2.connect(
   database=os.getenv("DBNAME"), 
   user=os.getenv("DBUSER"), 
   password=os.getenv("DBPASSWORD"), 
   host=sys.argv[1], 
   port= '5432'
)

cursor = conn.cursor()

cursor.execute("select version()")
data = cursor.fetchone()
print("version: ", data)

conn.close()