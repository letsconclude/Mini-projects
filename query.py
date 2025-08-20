from google.auth import compute_engine
from google.cloud import bigquery
from google.oauth2 import service_account
# create a credentials object from the service account file
credentials = service_account.Credentials.from_service_account_file('qwiklabs-gcp-04-655a7c046bec-0b0dd5a9083c.json')

#create a BigQuery client with the credentials
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

# Define the query to run
query = '''
insert into `qwiklabs-gcp-04-655a7c046bec.mytestdata.testdata` (name,age)
values ('baba', 20), ('gana', 21), ('pana', 22), ('yana', 23), ('bau', 24), ('kow', 25), ('ppt', 26), ('rsumitavi', 27);
SELECT
  *
FROM
  `qwiklabs-gcp-04-655a7c046bec.mytestdata.testdata`;
'''

print(client.query(query).to_dataframe())