import csv

def expand_database_fun(fname,vklist):
#def expand_database_fun():
     
    filename=fname
    v=vklist
    #filename='test.csv'
    #v=['loose','weight','in','7','days','and']
    
    #print(filename)
    #print(v)
    fields=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
    ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
    ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    
    
    for i in range(0,len(v)):
        #print(i)
        fields[i]=[v[i]]
        #print(i,' =',fields[i])
    #print(fields)

    with open(filename, 'a') as csvfile:
    #with open(filename, 'w') as csvfile:
    # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        for i in range(0,len(v)):
            if(fields[i]!=['and'] and fields[i]!=['is'] and fields[i]!=['am'] and fields[i]!=['are'] and fields[i]!=['and'] and fields[i]!=['not'] and fields[i]!=['0'] and fields[i]!=['1'] and fields[i]!=['2'] and fields[i]!=['3'] and fields[i]!=['4'] and fields[i]!=['5'] and fields[i]!=['6'] and fields[i]!=['7'] and fields[i]!=['8'] and fields[i]!=['9'] and fields[i]!=['10'] and fields[i]!=['30'] and fields[i]!=['a'] and fields[i]!=['A'] and fields[i]!=['with'] and fields[i]!=['for']and fields[i]!=['or'] and fields[i]!=['to'] and fields[i]!=['by'] and fields[i]!=['with'] and fields[i]!=['without'] and fields[i]!=['in'] and fields[i]!=['days'] and fields[i]!=['weeks'] and fields[i]!=['months']and fields[i]!=['month']and fields[i]!=['week'] and fields[i]!=['day']):
                #print(fields[i])
                csvwriter.writerow(fields[i])
        print("DATABASE UPDATED SUCCUSSFULLY")
   
#expand_database_fun()
