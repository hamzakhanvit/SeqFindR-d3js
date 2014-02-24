import numpy as np
import csv


matrix=[]  
reorder_row_matrix=[]  
strain_labels=[]   
vfs_list_xlabels=[]
index_file=[]
#Reading the values into matrices and lists                           
with open('matrix.csv', 'rb') as m, open('extra_stuff/reorderedrowmatrix.txt', 'rb') as rrm,open('extra_stuff/strain_labels.txt', 'rb') as sl,open('extra_stuff/vfs_list_xlabels.txt', 'rb') as vfs, open('index.txt', 'rb') as index:   
  for row in rrm:
    reorder_row_matrix.append(row.strip('\n'))
  for row in sl:
    strain_labels.append(row.strip('\n'))
  for row in index:
     index_file.append(row.strip('\n'))
  for row in vfs:
    vfs_list_xlabels.append(row.strip('\n'))           
  reader = csv.reader(m)
  for row in reader:
      matrix.append(row)
print "matrix-------------"
print matrix      
print "\nreorder_row_matrix------------"
print reorder_row_matrix
print "\n strain labels"
print strain_labels
print "\n vfs_xlabel"
print vfs_list_xlabels  
print "\n Index file"
print index_file                            
#making a dictionary of strain_labels and their index number.The present matrix is alteretered with its help.            
dictionary={}
for i in range(len(strain_labels)):
  dictionary[strain_labels[i]]=i;
print "the index dictionary is\n"
print dictionary
#declaring new matrix and list for storing the altered data as per the input index file.
new_matrix=[]  
new_strain_labels=[] 
#altering data as per the input index file
for row in index_file:
 print row
 print dictionary[row]
 new_matrix.append(matrix[dictionary[row]])
 new_strain_labels.append(strain_labels[dictionary[row]])
#print "new_matrix########################################"
#print new_matrix

trmatrix=[]
trmatrix=zip(*new_matrix)
trmatrix=zip(*trmatrix)
trmatrix=np.array(trmatrix)
print trmatrix[0][1] 
print "transverse matrix-------------"
print trmatrix  
fo = open("data.js", "wb")
fo.write( "var maxData=0.6000000000000000000;\nvar minData=-1.599999999999999944;\nvar data = [");
for i in range(int(len(trmatrix))):
        fo.write("[");
        for j in range(int(len(trmatrix[i]))):
            fo.write("[");
            c=float(trmatrix[i][j])
            print c
            fo.write(str(c));
            fo.write(", ");
            fo.write(str(i));
            fo.write(", ");
            fo.write(str(j));
            if(j!=(int(len(trmatrix[i])-1))):
               fo.write("], ");
            else:
               fo.write("]")   
        if(i!=(int(len(trmatrix))-1)):
            fo.write("],");
        else:
            fo.write("]");    
fo.write("];\n");
fo.write("var cols = [");
for a in range(int(len(vfs_list_xlabels))):
  fo.write("'");
  b = (vfs_list_xlabels[a]).translate(None, " '?.!/;:")
  fo.write(str(b));
  fo.write("'");
  if(a!=int(len(vfs_list_xlabels))-1):
    fo.write(", ");  
fo.write("];\n");

fo.write("var rows = [");
for a in range(int(len(new_strain_labels))):
  fo.write("'");
  fo.write(str(new_strain_labels[a]));
  fo.write("'");
  if(a!=int(len(new_strain_labels))-1):
    fo.write(", ");  
fo.write("];\n");
        
