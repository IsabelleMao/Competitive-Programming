#Create a table of differences!
def difference_maker(table, new_table):
  for i in range(len(table)):
    if i != len(table) - 1: #if it's not currently at the last number
        temp = table[i]
        next_temp = table[i+1]
        change = next_temp - temp #The difference in temperatures
        new_table.append(change) #Add all temperature changes here

#Change input to table
def fix_shit(shit):
  new = shit.split(" ") #Split into a list of strings
  new = [int(x) for x in shit] #Split into a list of integers
  items = new.pop(0) #remove the first number 'cause that's the length
  return new, items

        
def fubar():
    while True:
        raw_entered = input()
        if raw_entered == "0":
            break  # End when the input is 0
        else:
            #Define variables
            temperatures, length = fix_shit(raw_entered) #but mostly we'll be using temperatures
            differences = [] #TABLE OF TEMPERATURE DIFFERENCES!
            difference_maker(temperatures, differences)
            first_difference = differences[0]
            pattern = [] #Table for the longest pattern
            pattern.append(first_difference) #add first_difference to the pattern
            longest_cycle = 1 #the longest cycle of global warmingness
            for i in differences:
              if i == 0:
                continue #skip the current iteration if it's at the first difference
              

fubar()
