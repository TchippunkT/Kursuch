
def _delElement( arrays, i ):
    for array in arrays:
        del array[i]
    return arrays

def _searchStr( data, field, number ):
    if field:
        for index in range( len(data[number])-1, -1, -1 ):
            
            if str(field) == str(data[number][index]):
                pass
            else:
                data = _delElement(data, index)
        
    return data


def search( data, fields, numbers   ):

    for field, number in zip(fields, numbers):
        data = _searchStr( data, field, number )
        print(data)
    return data

    
    

        

        
        
        

        

        
