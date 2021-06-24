# PythonDictionaryScraper
this Python script enables the user to find meaning of words from www.dictionary.com and store them into a .docx file.


Common issue with this script is that once every one or two days, it cannot scrape the meaning of the word.

This is caused by the website's continually changing class attribute. 
To fix this:
1. Go to dictionary.com and type in a word
2. Highlight the first meaning
3. Right click and inspect 
4. You should see inside the <span class_ = "some_random_string">
5. Copy the "some_random_string" and replace it with inside the class_ = "some_random_string" on the 11th line of the code 
