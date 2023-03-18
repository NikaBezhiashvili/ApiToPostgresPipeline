import Country_Data
import DBMS

# --------------------------------------------------------- Create Table --------------------------------------------------------- #

def process_database():
    DBMS.create_table_business(DBMS.cursor, 'Business')
    DBMS.create_table_contact(DBMS.cursor, 'Contacts')
    DBMS.create_table_locations(DBMS.cursor, 'Locations')


# --------------------------------------------------------- Insert Into Business Table --------------------------------------------------------- #


def process_new_busniess():
    try:
        for i in Country_Data.mainData: 
                Warning_Record = i
                try:
                    Data_Insert = [i['id'],i['name'],i['is_closed'],i['review_count'],i['price'], i['rating']]
                except:
                    Data_Insert = [i['id'],i['name'],i['is_closed'],i['review_count'],'0','0']
                if DBMS.select_check(DBMS.cursor, i['id'], 'Business'):
                     pass
                else:
                    DBMS.insert_business(DBMS.cursor, Data_Insert)
    except:
         print(Warning_Record)
       
# --------------------------------------------------------- Insert Into Contacts Table --------------------------------------------------------- #


def process_new_contact():
    try:
        for i in Country_Data.mainData: 
                Warning_Record = i
                Data_Insert = [i['id'],i['image_url'],i['url'],i['phone'],i['display_phone']]
                if DBMS.select_check(DBMS.cursor, i['id'], 'Contacts'):
                     pass
                else:
                    DBMS.insert_contact(DBMS.cursor, Data_Insert)              
    except:
        print(Warning_Record)
        
# --------------------------------------------------------- Insert Into Locations Table --------------------------------------------------------- #

def process_new_locations():
    try:
        for i in Country_Data.mainData: 
                Warning_Record = i
                Data_Insert = [i['id'],i['coordinates']['latitude'],i['coordinates']['longitude'],i['location']['address1'],i['location']['address2'], i['location']['address3'], i['location']['city'], i['location']['zip_code'], i['location']['state'], i['location']['display_address'][0],  i['distance']]
                if DBMS.select_check(DBMS.cursor, i['id'], 'Locations'):
                     pass
                else:
                    DBMS.insert_locations(DBMS.cursor, Data_Insert)              
    except:
        print(Warning_Record)
        print('Failed')



