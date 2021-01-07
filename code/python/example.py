# pip3 install neo4j-driver
# python3 example.py

from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
  "bolt://<HOST>:<BOLTPORT>", 
  auth=basic_auth("<USERNAME>", "<PASSWORD>"))

cypher_query = '''
MATCH (u:User {screen_name: 'queenofthewo'})-[:POSTED]->(t:Tweet)-[:HAS_TAG]->(ht:Hashtag {tag:$tag}) 
RETURN t.created_str as createdTime
'''

with driver.session(database="neo4j") as session:
  results = session.read_transaction(
    lambda tx: tx.run(cypher_query,
      tag="thingsdonebymistake").data())

  for record in results:
    print(record['createdTime'])

driver.close()