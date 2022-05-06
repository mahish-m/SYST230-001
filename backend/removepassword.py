def removepassword(key):
    decrypt("Vault.csv",key)
    df=pd.read_csv(r"Vault.csv")
    table = df.values.tolist()
    newCompany = input("Password Name: ")
    for x in table:
        if newCompany in x:
            table.remove(x)
    
    pd.DataFrame(table).to_csv("Vault.csv",index=False)
    encrypt("Vault.csv", getFernetKey("Input Password to Save Changes"))#then encrypt it again
