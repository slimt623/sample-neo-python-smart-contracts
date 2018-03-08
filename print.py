# IMPORT
# import contract smartContracts/01-print.avm "" 01 False False
#
# INVOKE
# testinvoke <your_contract_hash>
#
# BUILD TEST
# build smartContracts/print.py test "" 01 False False

def Main(operation):

    if operation == 'create':
         create = create("test")
         return create
    elif operation == 'delete':
     	 delete = delete("yes")
     	 return delete
    else :
    	return False



def create(one):
    print(one)


def delete(two):
    print(two)
