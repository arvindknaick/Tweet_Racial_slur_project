
racial_words=["nigga","black","white","damn","hispanics","dark skinned"
              ,"chinks","white skinned","pakis","slave","slut","nigger"]                                         # Set words that indicate racial slur in list #

file=open("Tweet_text_file.txt","r")                                                                             # It is assumed that each tweet is in each  #
count=0                                                                                                          # line in the text file, it is opened       #          #

def profanity_level():                                                                                           # Function defined for printing the        #
     print()                                                                                                     # profanity level                          #    
     print("Profaniry score : ",racial_count)                                                                    
     if racial_count==0:                                                                                    
        print("Profanity level : Nil")       
     elif racial_count==1:
        print("Profanity level : low")
     elif racial_count==2:
        print("Profanity level : Medium")
     elif racial_count>=3:
        print("Profanity level : High")
     print()
     
while True:                                                                                                      # Loop for reading each tweet from the file #  
    
    count=count+1
    
    racial_count=0
     
    line=file.readline()
    if not line:
         break
    line_1="Tweet {}:\n\n {}".format(count,line.strip())
    
    print(line_1)
                                                                                                                # The tweet is cleaned by eliminating all  # 
    line_1=line_1.replace(",","")                                                                               # unwanted characters                      #
    line_1=line_1.replace(".","")                                                                                                 
    line_1=line_1.replace("'","")
    line_1=line_1.replace("?","")
    line_1=line_1.replace("/","")
    line_1=line_1.replace('"',"")
    line_1=line_1.lower()                                                                                       # The cleaned tweet is lower cased to detect  #
                                                                                                                # words in the given list clearly so no word  #
    for j in racial_words:                                                                                      # is missed                                
        if j in line_1:
            racial_count=racial_count+1                                                                         # Loop function for calculating the score of  #
                                                                                                                # racial words and profanity level            #                                                                                 
    profanity_level()
   
file.close()                                                                                                    # Closing the file                            #


