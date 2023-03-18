import ETL
import DBMS

ETL.process_database()
ETL.process_new_busniess()
ETL.process_new_contact()
ETL.process_new_locations()
DBMS.conn.close()
