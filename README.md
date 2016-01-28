# Powerball
A group of programs which allow for simulated Powerball drawings and determining which are the five most common white balls and the most common Powerball.

*powerball.py* simulates a user specified amount of Powerball drawings and writes them to a text file with a user specified name. This is multithread compatible, however, with 8 threads running, there are errors in the resultant text file as the program is too fast for the file handeler.

*powerballanalyzer.py* analyzes a selected text file to determine the five most common white balls and the most common Powerball.