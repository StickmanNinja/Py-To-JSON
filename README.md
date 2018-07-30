# Python to JSON Library

I wrote this library as a proof-of-concept project. There are other libraries that accomplish basically the same tasks. Yet in spite of this, I still wanted to develop my own approach to Python to JSON conversion. 

Not only did I finish what I set out to do, but my code is actually quite a bit faster than I expected it to be.

I tested the speed of my library compared to the popular “JSON” module. In 100 trials, my code won the speed test 98 times. It wasn’t even close. 

In fact, my code ran almost 220% faster.

If you want to do your own speed test, I would love to hear about the results.

## Usage Example
First, you need to place the file in your project. There are many ways you can do this, two of them being:

1. Placing code directly in your python project (.py) file.
2. Placing code in same folder of python (.py) file and referencing it with “from pytojson import *”

After doing one of these, you’re all set. You can now convert your dictionary with the following code:

`convert = Convert()`

`convert.Begin(WHATEVER DICTIONARY YOU WANT TO CONVERT)`