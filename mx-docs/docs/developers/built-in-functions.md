---
id: built-in-functions
title: Built-In Functions
---

[comment]: # (mx-abstract)

## **Introduction**

MultiversX protocol has a set of built-in functions. A built-in function is a special protocol-side function that doesn't
require a specific smart contract address as receiver of the transaction. When such a function is called via a transaction,
built-in handlers are triggered and will execute it.

Calls to these functions are considered `built-in function calls` and are treated different than other smart contract calls.

This documentation is subject to change, but at the time of writing, the current built-in functions were:

- ClaimDeveloperRewards
- ChangeOwnerAddress
- SetUserName
- SaveKeyValue
- ESDTTransfer
- ESDTBurn
- ESDTFreeze
- ESDTUnFreeze
- ESDTWipe
- ESDTPause
- ESDTUnPause
- ESDTSetRole
- ESDTUnSetRole
- ESDTSetLimitedTransfer
- ESDTUnSetLimitedTransfer
- ESDTLocalBurn
- ESDTLocalMint
- ESDTNFTTransfer
- ESDTNFTCreate
- ESDTNFTAddQuantity
- ESDTNFTBurn
- ESDTNFTAddURI
- ESDTNFTUpdateAttributes
- MultiESDTNFTTransfer

[comment]: # (mx-context-auto)

## **ClaimDeveloperRewards**

This function is to be used by Smart Contract owners in order to claim the fees accumulated during smart contract calls.
Currently, the developer reward is set to 30% of the fee of each smart contract call.

```rust
ClaimDeveloperRewardsTransaction {
    Sender: <the owner of the SC>
    Receiver: <SC address>
    Value: 0
    GasLimit: 6_000_000
    Data: "ClaimDeveloperRewards"
}
```

_For more details about how arguments have to be encoded, check [here](/developers/sc-calls-format)._

:::note
The amount of available developer rewards can be viewed via [Get Address](/sdk-and-tools/rest-api/addresses/#get-address) endpoint when using the smart contract as the `bech32Address`.
:::

[comment]: # (mx-context-auto)

## **ChangeOwnerAddress**

`ChangeOwnerAddress` is the function to be called by a Smart Contract's owner when a new owner is desired.

```rust
ChangeOwnerAddressTransaction {
    Sender: <the current owner of the SC>
    Receiver: <SC address>
    Value: 0
    GasLimit: 6_000_000
    Data: "ChangeOwnerAddress" +
          "@" + <new owner address in hexadecimal encoding>
}
```

_For more details about how arguments have to be encoded, check [here](/developers/sc-calls-format)._

[comment]: # (mx-context-auto)

## **SetUserName**

`SetUserName` is used to set an username for a given address. The receiver's address has to be the DNS smart contract
address of the address.

```rust
SetUserNameTransaction {
    Sender: <sender>
    Receiver: <DNS address that corresponds to the sender>
    Value: 0
    GasLimit: 1_200_000
    Data: "SetUserName@" +
          "@" + <username in hexadecimal encoding>
}
```

_For more details about how arguments have to be encoded, check [here](/developers/sc-calls-format)._

[comment]: # (mx-context-auto)

## **SaveKeyValue**

`SaveKeyValue` is used to store a given key-value under an address's storage. More details and the transaction's format are
already covered [here](/developers/account-storage).

[comment]: # (mx-context-auto)

## **ESDT and NFT built-in functions**

Most of the ESDT and NFT related built-in function are already described in the [ESDT](/developers/esdt-tokens/) and
[NFT](/developers/nft-tokens) sections.
