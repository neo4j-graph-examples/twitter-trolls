// npm install --save neo4j-driver
// node example.js
const neo4j = require('neo4j-driver');
const driver = neo4j.driver('bolt://<HOST>:<BOLTPORT>',
                  neo4j.auth.basic('<USERNAME>', '<PASSWORD>'), 
                  {/* encrypted: 'ENCRYPTION_OFF' */});

const query =
  `
  MATCH (u:User {screen_name: 'queenofthewo'})-[:POSTED]->(t:Tweet)-[:HAS_TAG]->(ht:Hashtag {tag:$tag})
  RETURN t.created_str as createdTime
  `;

const params = {"tag": "thingsdonebymistake"};

const session = driver.session({database:"neo4j"});

session.run(query, params)
  .then((result) => {
    result.records.forEach((record) => {
        console.log(record.get('createdTime'));
    });
    session.close();
    driver.close();
  })
  .catch((error) => {
    console.error(error);
  });
