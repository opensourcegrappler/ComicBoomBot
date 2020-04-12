import re
import sys
import os

def makepic(text,colour,longword):

    infile = 'bang.svg'
    outfile = 'outfile.svg'
    print(text)
    with open(infile) as file: # Use file to refer to the file object
        data = file.readlines()

        with open(outfile,'w') as ofile:
        
            for line in data:
                line = re.sub('FOO',text,line.rstrip())
                line = re.sub('#0000ff',colour,line.rstrip())
                if longword==True:
                    line = re.sub("font-size=\"16\"","font-size=\"10\"",line.rstrip())
            
                ofile.write(line)
                
    os.system('inkscape -z outfile.svg -e outfile_'+text+'.png')
    os.system('rm '+outfile)

#makepic("longwords",'',True)
