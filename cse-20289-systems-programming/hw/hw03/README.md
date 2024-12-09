# Group
| **Name** | **Email** |
| --- | --- |
| Aaron Wang | awang27@nd.edu |
| Derick Shi | dshi2@nd.edu |
| Ethan Little | elittle2@nd.edu |

# Installed packages:
python3 -m pip install python-docx

python3 -m pip install numpy

python3 -m pip install matplotlib


# Task 3.1
We chose to first filter the data because this way the sorting function has less data to sort throug and thus will be faster.

# Task 7
What happens if the URL does not fetch anything? Valid / good JSON?

* Program exits and prints 'Invalid URL'

What if the year / month request has no data after filtering?

* If no data is in the filtered set, an error message will be displayed and no document will be made

Could any of the stastical functions fail with insufficient data?

* Yes, so if no data, stats will be an empty dictionary

What should happen if the Word file already exists?

* We will overwrite the file

# Extra Credit

We decided to output all the stats and the text file the same way. We then printed the month and a bar graph for each month with statistics in the data set.