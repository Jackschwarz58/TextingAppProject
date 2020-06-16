# Programming Style Guide
> Consistency is key - Jack Schwarz (6-15-20)

#### All code written should adhere to the following styling guidelines


## Variable Naming

* All variable names must follow the snake case naming convention:<br>
(ex): `first_second` NOT `firstSecond`

* JSON data folows the same conventions<br>
(ex): `word_another: 'Two Words'`


* All final variables and auth codes should be uppercase (obviously):<br>
(ex): `THIS_IS_AN_IMPORTANT_VAR`

## Commenting

* All functions must have params detailed and a short descriptor on what it does above the function as a comment

## Command Line Output

* All potential known issues/code faults/errors must be handled and printed out to console with a __red__ `ERROR:` prefix.
![Imgur](https://i.imgur.com/Jw2dW1H.jpg)
* Notes are allowed when dealing with non-essential add-ons to command line output. This includes: CML ouput explanations, potential error points, reminders for checking external files/info, more info regarding error handling, or something that fits within this general description. All notes must be printed with a __yellow__ `NOTE:` prefix.
![Imgur](https://i.imgur.com/b7fh3wr.jpg)
* When printing out items like sucessful file reads, function completion, error avoidance, message callback confirms, or something that fits within this general description. All success messages must be printed with a __green__ `SUCCESS:` prefix.
![Imgur](https://i.imgur.com/nGRFKT2.jpg)

## General/Misc.

* Try to avoid long variable names and long function names, keep it simple
* Put any and all file specific details in the config file. DO NOT put file names or auth keys outside of this file! All variables in config should be considered confidential and remain hidden.

<br>

### When in doubt, [check here!](https://www.python.org/dev/peps/pep-0008/)
