# pip3 install neo4j
# python3 example.py

from neo4j import GraphDatabase, basic_auth

cypher_query = '''
MATCH (u:User {screen_name: 'queenofthewo'})-[:POSTED]->(t:Tweet)-[:HAS_TAG]->(ht:Hashtag {tag:$tag})
RETURN t.created_str as createdTime
'''

with GraphDatabase.driver(
    "neo4j://<HOST>:<BOLTPORT>",
    auth=("<USERNAME>", "<PASSWORD>")
) as driver:
    result = driver.execute_query(
        cypher_query,
        tag="thingsdonebymistake",
        database_="neo4j")
    for record in result.records:
        print(record['createdTime'])
