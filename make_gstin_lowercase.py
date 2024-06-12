gstin = input("Enter the GSTIN: ")
def check_GSTIN(gstin):
    is_al = "".join([i.lower() if gstin.isalpha else i for i in gstin])
    return is_al
    
print(check_GSTIN(gstin))
