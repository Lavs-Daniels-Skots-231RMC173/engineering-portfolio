[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18557949)
# DE0807_24_25P_ENG_T09

This task doesn't require input control, assume that user always inputs appropriate values unless stated othervise.

Output samples include text that should be output before/after the result. These samples are only approximation of one of possible results, as results are request dependant.


API is a mechanism that allows you to request information from online data source/web site.

It returns value/values that correspond to the request in JSON format. After turning that in to dictionary/list it is possible to access and manipulate these values.


This is the documentation for Game of Thrones API: https://gameofthronesquotes.xyz/

Your task is to create :
- an API request for:
  - 3 Tyrion quates 
  - 2 Jon Snow qoutes 
  - 1 random qoute. 
- All qoutes must be formatted before output, to not look like JSON, formatting is up to you.

1 point for API requests working 

1 point for looping trough results (for/while loops and no manual index/key numbers)

1 point for formatting.

(if API requests doesn't work and output - 0 points for the task)


Output sample for just one qoute:
```
'Leave one wolf alive and the sheep are never safe.'
          -- Arya Stark
```


Additional information:

https://realpython.com/python-requests/ - about API requests in general

https://docs.python.org/3/library/json.html - about JSON conversions
