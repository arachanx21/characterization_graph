def from_txt_to_csv(sourcefile,desired_filename):
    import csv
    import pandas as pd
    file=open(sourcefile,'r')
    raw_text=file.readlines()
    #x,y=raw_text[0].split(' ')
    #raw_text.close()
    for i in raw_text:
        text=i.split(' ')
        x=text[0]
        y=text[1]
        with open(desired_filename,"a") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow([x,y])
        print('adding: ',x,',',y,sep='')
    print(pd.read_csv(desired_filename))
    print('file',desired_filename,'created')
    print(pd.read_csv(desired_filename))
    print('file',desired_filename,'created')
    file.close()
    

#sourcefile=input("enter source file name: ")
#desired_filename=input("enter desired source file name: ")
#from_txt_to_csv(sourcefile,desired_filename)
