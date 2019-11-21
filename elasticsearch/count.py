from elasticsearch import Elasticsearch
import json

# connect
address_list = [{'host':'10.1.1.0', 'port':9000}]
es = Elasticsearch( address_list, timeout=60000 )

query_string = '''
{
  "fields": [],
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "term1": "value1"
          },
          "term": {
            "term2": "value2"
          },
          "term": {
            "term3": "value3"
          }
        }
      ],
      "must_not": [],
      "should": []
    }
  }
} 
'''


query_string = json.loads(query_string)
result = es.count(index="idx-201*",doc_type="pe_string",body=json.dumps(query_string))