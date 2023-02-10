---
id: es-index-miniblocks
title: miniblocks
---

[comment]: # (mx-abstract)

This page describes the structure of the `miniblocks` index (Elasticsearch), and also depicts a few examples of how to query it.

[comment]: # (mx-context-auto)

## _id

The _id field of this index is represented by the miniblock hash, in a hexadecimal encoding.

[comment]: # (mx-context-auto)

## Fields

| Field             | Description                                                                                                                                                                  |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| senderShard       | The senderShard field represents the shard ID of the source block.                                                                                                           |
| receiverShard     | The receiverShard field represents the shard ID of the destination block.                                                                                                    |
| senderBlockHash   | The senderBlockHash field represents the hash(hexadecimal encoded) of the source block in which the miniblock was included.                                                  |
| receiverBlockHash | The receiverBlockHash field represents the hash(hexadecimal encoded) of the destination block in which the miniblock was included.                                           |
| type              | The type field represents the type of the miniblock. It can be `TxBlock`(if it contains transactions) or `SmartContractResultBlock`(if it contains smart contracts results). |
| procTypeS         | The procTypeS field represents the processing type at the source shard. It can be `Normal` or `Scheduled`.                                                                   |
| procTypeD         | The procTypeD field represents the processing type at the destination shard. It can be `Normal` or `Scheduled`.                                                              |
| timestamp         | The timestamp field represents the timestamp of the block in which the miniblock was executed.                                                                               |
| reserved          | The reserved field ensures the possibility to extend the mini block.                                                                                                         |

[comment]: # (mx-context-auto)

## Query examples

[comment]: # (mx-context-auto)

### Fetch all the miniblocks of a block

```
curl --request GET \
  --url ${ES_URL}/miniblocks/_search \
  --header 'Content-Type: application/json' \
  --data '{
  	"query": {
		"bool": {
			"should": [
				{
					"match": {
						"senderBlockHash": "ddc..."
					}
				},
				{
					"match": {
						"receiverBlockHash": "ddc..."
					}
				}
			]
		}
	}
}'
```
