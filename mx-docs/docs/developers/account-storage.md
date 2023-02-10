---
id: account-storage
title: Account storage
---

[comment]: # (mx-abstract)

## Description

The MultiversX protocol offers the possibility of storing additional data under an account as key-value pairs. This can be useful for many use cases.

A wallet owner can store key-value pairs by using the built-in function `SaveKeyValue` that receives any number of key-value pairs.

:::tip
Keys that begin with `ELROND` will be rejected because they are reserved for protocol usage.
:::

[comment]: # (mx-context-auto)

## Transaction format

```rust
SaveKeyValueTransaction {
    Sender: <account address of the wallet owner>
    Receiver: <same as sender>
    Value: 0
    GasLimit: <required_gas>
    Data: "SaveKeyValue" +
          "@" + <key in hexadecimal encoding> +
          "@" + <value in hexadecimal encoding> +
          "@" + <key in hexadecimal encoding> +
          "@" + <value in hexadecimal encoding> +
          ...
}
```

_For more details about how arguments have to be encoded, check [here](/developers/sc-calls-format)._
[comment]: # (mx-context)
The gas used is computed as following:

```rust
required_gas =  save_key_value_cost +
                move_balance_cost +
                cost_per_byte * length(txData) +
                persist_per_byte * length(key) +   // repeated if multiple pairs
                persist_per_byte * length(value) + // repetead if multiple pairs
                store_per_byte * length(value) +   // repeated if multiple pairs
```

For a real case example, the cost would be:

`SaveKeyValue@6b657930@76616c756530` would cost `271000` gas units.

If we break down the gas usage operations, using the costs in the moment of writing, we would get:

```rust
required_gas =  100000    + // save key value function cost
                50000     + // move balance cost
                1500 * 34 + // cost_per_byte * length(txData)
                1000 * 4 + // persist_per_byte * length(key)
                1000 * 6 + // persist_per_byte * length(value)
                10000 * 6 + // store_per_byte * length(value)

             =  271000
```

[comment]: # (mx-context-auto)

## Example

Let's save a single key-value pair. Key would be `key0` and the value would be `value0`.

```rust
SaveKeyValueTransaction {
    Sender: <account address of the wallet owner>
    Receiver: <same as sender>
    Value: 0
    GasLimit: 271000
    Data: "SaveKeyValue" +
          "@" + 6b657930 +    // key0
          "@" + 76616c756530  // value0
}
```

_For more details about how arguments have to be encoded, check [here](/developers/sc-calls-format)._

[comment]: # (mx-context-auto)

## REST API

There are two endpoints that can be used for fetching key-value pairs for an account. They are:

- [Get value for key](/sdk-and-tools/rest-api/addresses/#get-storage-value-for-address)
- [Get all key-value pairs](/sdk-and-tools/rest-api/addresses/#get-all-storage-for-address)
