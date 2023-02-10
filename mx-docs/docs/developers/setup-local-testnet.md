---
id: setup-local-testnet
title: Setup a Local Testnet
---
[comment]: # (mx-abstract)

This guide describes how to set up a local mini-testnet using **mxpy**. The purpose of a local mini-testnet is to allow developers to experiment with and test their Smart Contracts, in addition to writing unit and integration tests.

The mini-testnet contains:

- **Validator Nodes** (two, by default)
- **Observer Nodes** (two, by default)
- A **Seednode**
- A **MultiversX Proxy**

If not specified otherwise, the mini-testnet starts with one Shard plus the Metachain (each with one Validator and one Observer).

[comment]: # (mx-context-auto)

## **Prerequisites: mxpy**

In order to install mxpy, follow the instructions at [install mxpy](/sdk-and-tools/sdk-py/installing-mxpy#install-using-mxpy-up-recommended).

[comment]: # (mx-context-auto)

## **Prerequisites: Node and Proxy**

Run the following command, which will fetch the prerequisites (`mx-chain-go`, `mx-chain-proxy-go`, `golang` and `testwallets`) into `~/multiversx-sdk`:

```bash
$ mxpy testnet prerequisites
```

[comment]: # (mx-context-auto)

## **Testnet Configuration**

Let's configure the following network parameters in mxpy, so that subsequent command invocations (of mxpy) will not require you explicitly provide the `--proxy` and `--chainID` arguments:

```bash
$ mxpy config set chainID local-testnet
$ mxpy config set proxy http://localhost:7950
```

Then, in a folder of your choice add a file names `testnet.toml` with the content below.

```bash
$ mkdir MySandbox && cd MySandbox
$ touch testnet.toml
```

```
testnet.toml
[networking]
port_proxy = 7950
```

:::tip
mxpy allows you to customize the configuration of the local mini-testnet in much greater detail, but for the sake of simplicity, in the example above we've only set the TCP port of the MultiversX Proxy.
:::

Then, configure and build the local testnet as follows:

```bash
$ cd MySandbox
$ mxpy testnet config
```

Upon running this command, a new folder called `testnet` will be added in the current directory. This folder contains the Node & Proxy binaries, their configurations, plus the **development wallets**.

:::caution
The development wallets (Alice, Bob, Carol, ..., Mike) **are publicly known** - they should only be used for development and testing purpose.
:::

The development wallets are minted at genesis and their keys (both PEM files and Wallet JSON files) can be found in the folder `testnet/wallets/users`.

[comment]: # (mx-context-auto)

## **Starting the Testnet**

```bash
mxpy testnet start
```

This will start the Seednode, the Validators, the Observers and the Proxy.

:::important
Note that the Proxy starts with a delay of about 30 seconds.
:::

[comment]: # (mx-context-auto)

## **Sending transactions**

Let's send a simple transaction using **mxpy**:

```
Simple Transfer
mxpy tx new --recall-nonce --data="Hello, World" --gas-limit=70000 \
 --receiver=erd1spyavw0956vq68xj8y4tenjpq2wd5a9p2c6j8gsz7ztyrnpxrruqzu66jx \
 --pem=~/multiversx-sdk/testwallets/latest/users/alice.pem \
 --send
```

You should see the prepared transaction and the **transaction hash** in the `stdout` (or in the `--outfile` of your choice). Using the transaction hash, you can query the status of the transaction against the Proxy or against mxpy itself:

```bash
$ curl http://localhost:7950/transaction/1dcfb2227e32483f0a5148b98341af319e9bd2824a76f605421482b36a1418f7
$ mxpy tx get --hash=1dcfb2227e32483f0a5148b98341af319e9bd2824a76f605421482b36a1418f7
```

[comment]: # (mx-context-auto)

## **Deploying and interacting with Smart Contracts**

Let's deploy a Smart Contract using **mxpy**. We'll use the simple Counter as an example.

If you need guidance on how to build the Counter sample contract, please follow the [Counter SmartContract Tutorial](/developers/tutorials/counter).

```rust
Deploy Contract
mxpy --verbose contract deploy --bytecode=./counter.wasm \
 --recall-nonce --gas-limit=5000000 \
 --pem=~/multiversx-sdk/testwallets/latest/users/alice.pem \
 --outfile=myCounter.json \
 --send
```

Upon deployment, you can check the status of the transaction and the existence of the Smart Contract:

```bash
$ curl http://localhost:7950/transaction/0db61bab8e78779ae009300988c6be0949086d93e2b7adfddd5e6375a4b6eeb7 | jq
$ curl http://localhost:7950/address/erd1qqqqqqqqqqqqqpgqj5zftf3ef3gqm3gklcetpmxwg43rh8z2d8ss2e49aq | jq
```

If everything is fine (transaction status is `executed` and the `code` property of the address is set), you can interact with or perform queries against the deployed contract:

```
Call Contract
mxpy --verbose contract call erd1qqqqqqqqqqqqqpgqj5zftf3ef3gqm3gklcetpmxwg43rh8z2d8ss2e49aq \
 --recall-nonce --gas-limit=1000000 --function=increment \
 --pem=~/multiversx-sdk/testwallets/latest/users/alice.pem --outfile=myCall.json \
 --send

```

```
Query Contract
mxpy --verbose contract query erd1qqqqqqqqqqqqqpgqj5zftf3ef3gqm3gklcetpmxwg43rh8z2d8ss2e49aq --function=get
```

[comment]: # (mx-context-auto)

## **Simulating transactions**

At times, you can simulate transactions instead of broadcasting them, by replacing the flag `--send` with the flag `--simulate`. For example:

```
Simulate: Call Contract
all-nonce --gas-limit=1000000 --function=increment \
 --pem=~/multiversx-sdk/testwallets/latest/users/alice.pem --outfile=myCall.json \
 --simulate
```

```
Simulate: Simple Transfer
mxpy tx new --recall-nonce --data="Hello, World" --gas-limit=70000 \
 --receiver=erd1spyavw0956vq68xj8y4tenjpq2wd5a9p2c6j8gsz7ztyrnpxrruqzu66jx \
 --pem=~/multiversx-sdk/testwallets/latest/users/alice.pem \
 --simulate
```
