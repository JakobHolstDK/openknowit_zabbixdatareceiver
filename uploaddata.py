#!/usr/bin/env python

import json
import psycopg2
import pprint

from datetime import datetime

# Database connection parameters
db_params = {
    'dbname': 'dash',
    'user': 'dash',
    'password': 'hu8jmn3',
    'host': 'dashdb01.openknowit.com',
    'port': '5432'
}

# File path
file_path = '/var/lib/dash/history.ndjson'

def parse_json_line(line):
    try:
        data = json.loads(line)
        return data
    except json.JSONDecodeError as e:
#        print(f"Error parsing JSON: {e}")

        return None

def insert_data(cursor, data, connection):
    try:
        formatted_datetime = datetime.fromtimestamp(data['clock']).strftime('%Y-%m-%d %H:%M:%S')
        statement = ""
        
        if ( data['type'] == 0 ):
          datatype = 0
          host_name = data['host']['name']
          itemid = data['itemid']
          itemname = data['name']
          ns = data['ns']
          value = data['value']
          statement = "INSERT INTO zabbix_data_type_0 (host_name, item_id, item_name, clock, ns, value, data_type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
          cursor.execute(statement, ( host_name, itemid, itemname, formatted_datetime, ns, value, datatype  ))
          connection.commit()

        if ( data['type'] == 1 ):
          datatype = 1
          host_name = data['host']['name']
          itemid = data['itemid']
          itemname = data['name']
          ns = data['ns']
          value = data['value']
          statement = "INSERT INTO zabbix_data_type_1 (host_name, item_id, item_name, clock, ns, value, data_type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
          cursor.execute(statement, ( host_name, itemid, itemname, formatted_datetime, ns, value, datatype  ))
          connection.commit()

        if ( data['type'] == 2 ):
            datatype = 2
            host_name = data['host']['name']
            itemid = data['itemid']
            itemname = data['name']
            ns = data['ns']
            value = data['value']
            statement = "INSERT INTO zabbix_data_type_2 (host_name, item_id, item_name, clock, ns, value, data_type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(statement, ( host_name, itemid, itemname, formatted_datetime, ns, value, datatype  ))
            connection.commit()

        if ( data['type'] == 3 ):
            datatype = 3
            host_name = data['host']['name']
            itemid = data['itemid']
            itemname = data['name']
            ns = data['ns']
            value = data['value']
            statement = "INSERT INTO zabbix_data_type_3 (host_name, item_id, item_name, clock, ns, value, data_type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(statement, ( host_name, itemid, itemname, formatted_datetime, ns, value, datatype  ))
            connection.commit()
        
        if ( data['type'] == 4 ):
            datatype = 4
            host_name = data['host']['name']
            itemid = data['itemid']
            itemname = data['name']
            ns = data['ns']
            value = data['value']
            json_data = json.loads(value)
            pprint.pprint(json_data)
            statement = "INSERT INTO zabbix_data_type_4 (host_name, item_id, item_name, clock, ns, fsname, options, bytes_used, bytes_free, bytes_total, bytes_pused, bytes_pfred, fstype, inodes_used, inodes_free, inodes_total, inodes_pused, inodes_pfree) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(statement, ( host_name, itemid, itemname, formatted_datetime, ns, json_data['fsname'], json_data['options'], json_data['bytes']['used'], json_data['bytes']['free'], json_data['bytes']['total'], json_data['bytes']['pused'], json_data['bytes']['pfree'], json_data['fstype'], json_data['inodes']['used'], json_data['inodes']['free'], json_data['inodes']['total'], json_data['inodes']['pused'], json_data['inodes']['pfree'] ))
            connection.commit()


    except psycopg2.Error as e:
        #print(f"Error inserting data: {e}")
        connection.rollback()
        
    


def main():
    # Connect to the database
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        # Read and upload data from the file
        with open(file_path, 'r') as file:
            for line in file:
                json_data = parse_json_line(line)
                if json_data:
                    insert_data(cursor, json_data, connection)

        # Commit the changes and close the connection
        connection.commit()
        print("Data uploaded successfully.")
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
    finally:
        if connection:
            connection.close()
    

if __name__ == "__main__":
    main()
