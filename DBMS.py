import psycopg2 as db

# --------------------------------------------------------- Connection --------------------------------------------------------- #

dbname = 'DBPost'
user = 'postgres'
password = 'admin'
host = 'localhost'
conn = db.connect(
    database = dbname,
    user = user,
    password = password,
    host = host
)

cursor = conn.cursor()


def commit():
    conn.commit()

# --------------------------------------------------------- Create Table --------------------------------------------------------- #

def create_table_business(cur, table : str):
    cur.execute("""Create table if not exists %s(
            id varchar(50) primary key not null,
            name varchar(200) default 'UNNAMED',
            status varchar(5) default 'A',
            review_count int,
            price varchar(10),
            rating int
    )"""%(table))

    commit()

def create_table_contact(cur, table : str):
    cur.execute("""Create table if not exists %s(
            id varchar(50) REFERENCES business (id),
            image_url varchar(250) default 'Not Found',
            website varchar(250) default 'Not Found',
            phone varchar(50) default 'Not Found',
            display_phone varchar(50) default 'Not Found'
    )"""%(table))


def create_table_locations(cur, table : str):
    cur.execute("""Create table if not exists %s(
            id varchar(50) REFERENCES business (id),
            latitude varchar(250) default 'Not Found',
            longitude varchar(250) default 'Not Found',
            address1 varchar(50) default 'Not Found',
            address2 varchar(50) default 'Not Found',
            address3 varchar(50) default 'Not Found',     
            city varchar(15) default 'Not Found',
            zip_code varchar(10) default 'Not Found',
            state varchar(20) default 'Not Found',
            display_address varchar(50) default 'Not Found',
            distance int default 0
    )"""%(table))



# --------------------------------------------------------- Insert Table --------------------------------------------------------- #

def insert_business(cur, values : list):
    cur.execute("insert into business values(%s, %s, %s, %s, %s,%s)", values)
    commit()


def insert_contact(cur, values : list):
    cur.execute("insert into Contacts values(%s, %s, %s, %s, %s)", values)
    commit()
    
def insert_locations(cur, values : list):
    cur.execute("insert into locations values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", values)
    commit()

# --------------------------------------------------------- Select Table --------------------------------------------------------- #


def select_check(cur, value : str, table : str):
    cur.execute(f"SELECT ID FROM {table} WHERE ID = '%s'"%(value))
    data = cur.fetchone()
    try:
        if data[0] == value:
            return True
        else:
            return False
    except: 
            return False
    


    commit()






