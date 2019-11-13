- **Author:** Vivek Khimani
- **Contact:** +12673049080
- **Purpose:** Interaction with CollectUpdatesContract (Federated Learning Research Paper)

---

## Required Installations:

- **web3** - "pip install web3"
- **ipfs-api** - "pip install ipfs-api"
- **local ipfs installation** - "https://docs.ipfs.io/guides/guides/install/"

## Files Information:

- **Participant_Details.csv** => csv file containing ethereum addresses and private keys of all the participants (ALL)
- **my_abi.json** => abi of the CollectUpdates contract stored in json format (VIVEK)
- **state_abi.json** => abi of the State contract stored in json format (VIVEK)
- **credentials.py** => formatted abis of both the contracts (VIVEK)
- **DeployContract.py** => used to store and create CollectUpdates contract instance (VIVEK)
- **DeployStateContract.py** => used to store and create State contract instance (VIVEK)
- **all_clients.py** => hash map (dictionary) containing address and private key of all clients (VIVEK & ABHISHEK)
- **whitelisted.py** => NEED TO BE GENERATED BY ABHISHEK using some AGENT SAMPLING MECHANISM. data structure is explained in the file. (ABHISHEK)
- **main.py** => calling interface for smart contract methods. FIND more details in INSTRUCTIONS section. (VIVEK & ABHISHEK)
- **ipfs_conn.py** => USED to establish connection with IPFS api and add the local updates to IPFS API and generate hashes.(VIVEK & ABHISHEK)
- **StoredHashes.py** => RUNS ipfs_conn.py functions and stores the generated hashes in a dictionary so it can be later used by ABHISHEK to retrieve the local update values (VIVEK & ABHISHEK)
- **updateGlobalState.py** => Saves the current global update model in the State smart contract when called (VIVEK & ABHISHEK)
- **getLocalAgentUpdates.py** => Uses the IPFS hashes (stored locally, no interaction with the hashes stored on the contract due to web3py bug) to get the local updates of all the participating agents (VIVEK & ABHISHEK)

## Instructions:

- Data for all the agents can be found in **all_clients.py** in a hashMap structure which is explained in the file.
- **ABHISHEK** needs to add REPUTATION SCORE data to the hashMap (if required).
- **ABHISHEK** needs to run an AGENT SAMPLING SCRIPT on **all_clients.py** that will sample whitelisted agents and put it in a data structure explained in **whitelisted.py**.
- Once the whitelisted agents are available (in the given format), **ABHISHEK** needs to run the script **main.py**. This will add the whitelisted agents to blockchain.

- **IPFS DAEMON** has to be activated at this stage on the local computer using IPFS-CLI. Please find it online. Should be straightforward.

- Later, **ABHISHEK** can run **getLocalAgentUpdates.py** (NOTE that this will run ipfs_conn.py implicity) which will serialize the local updates from each agent and add it to the IPFS, generate hashes, and store those hashes on the blockchain. Running this script, will enable ABHISHEK to get the LOCAL_UPDATES from all the whitelisted agents as a 2-D array and he can further use it for HYPERSPHERE BASED CLASSIFIER and other use cases.

## Global Update Storage Mechanism:

- NOTE that there is a file called **updateGlobalState.py**, which can be called by the SERVER to update the global updates on State smart contract. As a result, this file has to be used when the federated learning mechanism is updated.