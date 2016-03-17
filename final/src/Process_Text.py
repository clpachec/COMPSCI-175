'''
Created on Sun Mar  13 010:21:32 2016

@author: Arielle
'''

import re
import nltk

def Clean_Text(text: str):
    """
    Returns a string cleaned of non-word related characters such as <br/ <p> due to
    source of generated text

    Parameters
    ----------
    text : str
        Text to be cleaned and formatted.
        
    Returns
    -------
    str
        A formatted and cleaned string
        
    Examples
    --------
    >>> Clean_Text("<p>And upon Future could've Station  when.")
    "And upon Future could've Station when."
    --------
    ""
    """
    
    result = re.sub('((<\w*>)?(1)(<\w*>)|<\w*)|(\S*>)',' ',text) #Removes words such as <br/ <p>
    result = re.sub('&quot;',' ',result) #Remove '&quot;' artifact
    result = re.sub('\s\s+',' ',result) #Clean out the extra spaces created by the previous line

    return result