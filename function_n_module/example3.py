# there should be the local variable in the fuction if the variable is written outside of the function
data= " "

def data_appender(s):
    global data # data variable should be int the function
    if len(s)>0:
        data +=s
data_appender('hello')
data_appender('world')
data_appender('this is a simple function')
print(data)