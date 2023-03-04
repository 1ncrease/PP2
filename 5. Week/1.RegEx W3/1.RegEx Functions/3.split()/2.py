#You can control the number of occurrences by specifying the maxsplit parameter:

import re

#Split the string at the first white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
