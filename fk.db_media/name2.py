s=open("media", 'r');
l=s.read().split('"')[1::2];
e=l[0:][::2];
o=l[1:][::2];
for i in range(len(e)):
  print 'mv ';
  print e[i];
  print o[i];
  print ';';
