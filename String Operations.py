Name='Joel'
weight=80
str="this is string example.....wow!!"
str2="THIS IS STRING EXAPLE"

print "My name is %s and weight is %d kg!" % (Name,weight)
print"------------------------------------------"
print"str.capitalize() : ", str.capitalize()
#this works of make the first word in mayuscula
print"---------------------------------------"
print str2.lower()
print"-------------------------------------------"
suffix="wow!!"
print str.endswith(suffix)
print str.endswith(suffix,20)
# this works compare an word if is in the string
print"-------------------------------------------"
print str.replace("is","was")
print str.replace("is","was",3)

