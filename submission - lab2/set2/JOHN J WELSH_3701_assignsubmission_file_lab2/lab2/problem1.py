#Lab 2, Problem 1 by John Welsh

# 1.  store the following student records into a variable using list of tuples

# "jimmhy"  98   35  56
# "jones"   89   88	98
# "lucy"	  99   90   98

# print out jones' third subject score

student_records = [["jimhy", (98, 35, 56)], ["jones", (89, 88, 98)], ["lucy", (99, 90, 98)]]
print student_records[1][1][-1]