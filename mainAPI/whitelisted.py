#needs to be generated by ABHISHEK in this format using AGENT SAMPLING MECHANISM.
#whitelisted = {"ETHEREUM_ACCOUNT":"LOCALUPDATESARRAY"}

#####TO BE IGNORED BY ABHISHEK (DONE BY VIVEK FOR TESTING PURPOSES)#####
from all_clients import all_clients

def startWhitelisting(num_agents):
    counter = 0
    whitelisted = {}
    for items in all_clients.keys():
        if counter == num_agents:
            break
        whitelisted[items] = [0.5,0.5,0.5,0.5]
        counter+=1
    return whitelisted

whitelisted = startWhitelisting(12)

#whitelisted = {"0xfCb89072149b45ad9bbF698d15efA2283da8fd6f":[0.45,0.76,0.85,0.77],"0xEF84a3c5E2914De5FD235937351Ef73C1E4B9658":[0.85,0.64,0.75],"0x6E9b61CAAC3b61bA1bE990ea07Ebe1CcF2cCAb0D":[0.5,0.9,1.0],"0x1829EBC2FB3bD199225dc138913B18c39DAC762e":[0.9,0.8,0.7]}

##DRIVER##
if __name__ == '__main__':
    print(whitelisted)