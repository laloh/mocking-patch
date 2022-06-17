import requests

import pandas as pd
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine


api_url = 'https://pokeapi.co/api/v2/pokemon/'


def get_pokemons(api_url):
	print(f"Getting Pokemons from: {api_url}")
	results = requests.get(api_url)
	return results.json()


def create_sf_engine():
	return create_engine(URL(
		account = 'xxxxx',
		user = 'xxxx',
		password = 'xxx',
		database = 'testdb',
		schema = 'public',
		warehouse = 'testwh',
		role='myrole',
	))
	

def insert_into_snowflake(batch, conn, table_name):
	success = False
	try:
		df = pd.DataFrame(batch)
		df.to_sql(table_name, con=conn, if_exists="append", index=False)
		success = True
	except Exception as e:
		print(e)
	
	return success

def delete_pokemon(conn, pokemon_name, table_name):
	success = False
	try:
		cur = conn.cursor()
		cur.execute(f"DELETE FROM {table_name} WHERE name = '{pokemon_name}'")
		conn.commit()
		success = True
	except Exception as e:
		print(e)

	return success 


if __name__ == "__main__":

	result = get_pokemons(api_url)
	engine = create_sf_engine()
	connection = engine.connect()
	
	insert_into_snowflake(result, connection, "pokemons")

	connection.close()
	engine.dispose()
