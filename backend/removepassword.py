from PassManager import *
def removepassword(key, passName):
    decrypt("Vault.csv",key)
    df=pd.read_csv(r"Vault.csv")
    table = df.values.tolist()
    for x in table:
        if passName in x:
            table.remove(x)
    pd.DataFrame(table).to_csv("Vault.csv",index=False)
    encrypt("Vault.csv", getFernetKey("Input Password to Save Changes"))#then encrypt it again
