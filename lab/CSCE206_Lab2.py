'''################################################################################
        CSCE 206 LAB - 2
                Lab -2 : Working with Tuples - Solution
                        
                Author:   Sendurr Selvaraj
                Email:    sendurr@hotmail.com
################################################################################'''

# Exercise 1 : Store the following student records into a variable using list of tuples
# "jimmhy"  98   35  56
# "jones"   89   88	98
# "lucy"	  99   90   98
# print out jones' third subject score

tup1 = ["jimmhy" ,98,35,56]
tup2 = ["jones" , 89,88,98]
tup3 = ["lucy",99,90,98]

print "Printing results of exercise 1 \n"
print " Jones third subject score is " + str(tup2[3])
print "exercise 1 completed \n \n"

# Exercise 2 : create a 3 dimension matrix of  3X3X3 and store it into M3 variable
# the values are
# 1	1	1
# 1	1	1
# 1	1	9

# 2	2	2
# 2	8	2
# 2	2	2
#print the 8, 9 using the M3 variable with indexes

print "Printing results of exercise 2 \n"

array1 = [[[1,1,1,],[1,1,1],[1,1,9]],
         [[2,2,2,],[2,8,2],[2,2,2]]]

print "The index to print " + str(array1[0][2][2]) + " is [0][2][2]"
print "The index to print " + str(array1[1][1][1]) + " is [1][1][1]"

print "exercise 2 completed \n \n"

# Exercise 3: Store student subject score for a student into a variable of dictionary
# jimmy's score
# physics: 58
# math:98
# english:98

        
jim_score = {'Physiscs':'58' , 'Maths':'98' , 'English' : '98'}
        
print "Printing results of exercise 3 \n"

for key in jim_score:
        print "Jimmy's " + key + " score is " + jim_score[key]

print "exercise 3 completed \n \n"

# Exercise 4 Store temperature of 10 cities into a variable  CityT
# specify your own city names.

city_temp = {'New York':'60' , 'Columbia':'72' , 'Boston' : '50', 'San Fransisco':'82','Houston':'84',
            'Atlanta':'72','Austin':'82','Phoenix':'84','Boston':'45' ,'chicago':'40'}
print "Printing results of exercise 4 \n"

for key in city_temp:
        print "The temperature at  " + key + " is " + city_temp[key] + "`F"

print "exercise 4 completed \n \n"


'''################################################################################
        End of Program
################################################################################'''
