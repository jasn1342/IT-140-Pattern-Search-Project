import re

#Paragraph provided for search and replace

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

#Place all the code from the previous steps here

#Part 1
regex="[^a-zA-Z\d]" #Asks to count all characters in the string except for letters and numbers.

#assign the outcome to the variable name "result."
result=re.findall(regex, lorem_ipsum)

#Output to console
print(len(result))


#Part 2
#get all of the instances of 'sit-amet' or 'sit:amet' characters in the string assigned to lorem_ipsum.
regex = "sit[-:]amet"

#Assign the outcome to a variable named occurrences_sit_amet
occurance_sit_amet=re.findall(regex, lorem_ipsum)

#Output to console
print(len(occurance_sit_amet))

#Part 3
#Replace sit:amet and sit-amet with sit amet using the re.sub() function.
regex="sit[-:]amet"

#Assign the outcome to a variable named replace_results
replace_results=re.sub(regex,"sit amet", lorem_ipsum)

#Assign the outcome to a variable named occurrences_sit_amet
occurance_sit_amet=re.findall(regex,lorem_ipsum)

#Output to console
print (len(occurance_sit_amet))

#Part 4
regex="sit[-:]amet"

replace_results=re.sub(regex,"sit amet", lorem_ipsum)

occurance_sit_amet=re.findall(regex,lorem_ipsum)

#Output to the console, the number of sit amet occurrences.
print (len(occurance_sit_amet))