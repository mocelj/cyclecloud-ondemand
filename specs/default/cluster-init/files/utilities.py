import subprocess
import yaml

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


def executeCommandList(commandList):   
    for command in commandList:
        subprocess.check_output(command.split(" "))


def readOnDemandConfiguration():
    with open('/etc/ood/config/ood_portal.yml', 'r') as fid:
        onDemandConfiguration = yaml.load(fid, Loader=yaml.Loader)  
    
    return onDemandConfiguration

def writeOnDemandConfiguration(configuration):
    with open('/etc/ood/config/ood_portal.yml', 'w') as fid:
        yaml.dump(configuration, fid)


def getSecretValue(keyVaultName, secretName):
    vaultURL = "https://" + keyVaultName + ".vault.azure.net"
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vaultURL, credential=credential)
    return client.get_secret(secretName).value