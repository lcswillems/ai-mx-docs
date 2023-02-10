---
id: counter
title: The Counter Smart Contract
---
[comment]: # (mx-abstract)
By following the tutorial on this page, you will learn how to write, build, and deploy a basic Smart Contract in C

[comment]: # (mx-context-auto)

## **Prerequisites**

You need to have [mxpy](/sdk-and-tools/sdk-py/installing-mxpy) installed.

[comment]: # (mx-context-auto)

## **Create the contract**

In a folder of your choice, run the following command:

```
mxpy contract new --template="simple-counter" mycounter
```

This creates a new folder named `mycounter` which contains the C source code for a simple Smart Contract - based on the template [simple-counter](https://github.com/multiversx/mx-sc-examples/tree/master/simple-counter). The file `counter.c` is the implementation of the Smart Contract, which defines the following functions:

- `init()`: this function is executed when the contract is deployed on the Blockchain
- `increment()` and `decrement()`: these functions modify the internal state of the Smart Contract
- `get()`: this is a pure function (does not modify the state) which we'll use to query the value of the counter

[comment]: # (mx-context-auto)

## **Build the contract**

In order to build the contract to WASM, run the following command:

```
mxpy --verbose contract build mycounter
```

Above, `mycounter` refers to the previously created folder, the one that holds the source code. After executing the command, you can inspect the generated files in `mycounter/output`.

[comment]: # (mx-context-auto)

## **Deploy the contract on the Testnet**

In order to deploy the contract on the Testnet you need to have an account with sufficient balance (required for the deployment fee) and the associated private key in **PEM format**.

The deployment command is as follows:

```
mxpy --verbose contract deploy --project=mycounter --pem="alice.pem" --gas-limit=5000000 --proxy="https://testnet-gateway.multiversx.com" --outfile="counter.json" --recall-nonce --send
```

Above, `mycounter` refers to the same folder that contains the source code and the build artifacts. The `deploy` command knows to search for the WASM bytecode within this folder.

Note the last parameter of the command - this instructs mxpy to dump the output of the operation in the specified file. The output contains the address of the newly deployed contract and the hash of the deployment transaction.

```
counter.json
{
    "emitted_tx": {
        "tx": {
            "nonce": 0,
            "value": "0",
            "receiver": "erd1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq6gq4hu",
            "sender": "erd1...",
            "gasPrice": 1000000000,
            "gasLimit": 5000000,
            "data": "MDA2MTczNmQwMTAwMDA...MDA=",
            "chainID": "T",
            "version": 1,
            "signature": "a0ba..."
        },
        "hash": "...",
        "data": "...",
        "address": "erd1qqqqqqqqqqqqqpgqp93y6..."
    }
}
```

Feel free to inspect these values in the [Explorer](https://explorer.multiversx.com/).

[comment]: # (mx-context-auto)

## **Interact with the deployed contract**

Let's extract the contract address from `counter.json` before proceeding to an actual contract execution.

```
export CONTRACT_ADDRESS=$(python3 -c "import json; data = json.load(open('counter.json')); print(data['emitted_tx']['address'])")
```

Now that we have the contract address saved in a shell variable, we can call the `increment` function of the contract as follows:

```
mxpy --verbose contract call $CONTRACT_ADDRESS --pem="alice.pem" --gas-limit=2000000 --function="increment" --proxy="https://testnet-gateway.multiversx.com" --recall-nonce --send
```

Execute the command above a few times, with some pause in between. Then feel free to experiment with calling the `decrement` function.

Then, in order to query the value of the counter - that is, to execute the `get` pure function of the contract - run the following:

```
mxpy contract query $CONTRACT_ADDRESS --function="get" --proxy="https://testnet-gateway.multiversx.com"
```

The output should look like this:

```
[{'base64': 'AQ==', 'hex': '01', 'number': 1}]
```

[comment]: # (mx-context-auto)

## **Interaction script**

The previous steps can be summed up in a simple script as follows:

```
#!/bin/bash

# Deployment
mxpy --verbose contract deploy --project=mycounter --pem="alice.pem" --gas-limit=5000000 --proxy="https://testnet-gateway.multiversx.com" --outfile="counter.json" --recall-nonce --send
export CONTRACT_ADDRESS=$(python3 -c "import json; data = json.load(open('address.json')); print(data['emitted_tx']['contract'])")

# Interaction
mxpy --verbose contract call $CONTRACT_ADDRESS --pem="alice.pem" --gas-limit=2000000 --function="increment" --proxy="https://testnet-gateway.multiversx.com" --recall-nonce --send
sleep 10
mxpy --verbose contract call $CONTRACT_ADDRESS --pem="alice.pem" --gas-limit=2000000 --function="increment" --proxy="https://testnet-gateway.multiversx.com" --recall-nonce --send
sleep 10
mxpy --verbose contract call $CONTRACT_ADDRESS --pem="alice.pem" --gas-limit=2000000 --function="decrement" --proxy="https://testnet-gateway.multiversx.com" --recall-nonce --send
sleep 10

# Querying
mxpy contract query $CONTRACT_ADDRESS --function="get" --proxy="https://testnet-gateway.multiversx.com"
```
