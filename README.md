# CleverDict

## Overview

```CleverDict``` is a hybrid Python data class which allows both ```object.attribute``` and ```dictionary['key']``` notation to be used simultaneously and interchangeably.  It's particularly handy when your code is mainly object-orientated but you want a 'DRY' and extensible way to import data in json/dictionary format into your objects... or vice versa... without having to write extra code just to handle the translation.

The class also optionally triggers a ```.save()``` method (which you can adapt or overwrite) which it calls whenever an attribute or dictionary value is created or changed.  This is especially useful if you want your results to be automatically pickled, encoded, saved to a file or database, uploaded to the cloud etc. with having to explicitly call your update function in every single function where attributes might change.


## Installation
No dependencies.  Very lightweight:

    pip install cleverdict

## Quickstart

```CleverDict``` objects behave like normal Python dictionaries, but with the convenience of immediately offering read and write access to their data (keys and values) using the ```object.attribute``` syntax, which many people find easier to type and more intuitive to read and understand:

    >>> from cleverdict import CleverDict
    >>> x = CleverDict({'total':6, 'usergroup': "Knights of Ni"})
    >>> x.total
    6
    >>> x['total']
    6
    >>> x.usergroup
    'Knights of Ni'
    >>> x['usergroup']
    'Knights of Ni'

You can also supply keyword arguments like this:

    >>> x = CleverDict(created = "today", review = "tomorrow")
    >>> x.created
    'today'
    >>> x['review']
    'tomorrow'

Regardless of which syntax you use, new values are immediately available via both methods:

    >>> x['life'] = 42
    >>> x.life += 1
    >>> x['life']
    43
    >>> del x['life']
    >>> x.life
    # KeyError: 'life'

You can import an existing object's data (but not its methods) directly using ```vars()```:

    x = CleverDict(vars(my_existing_object))
    >>> list(x.items())
    [('total', 6), ('usergroup', 'Knights of Ni'), ('life', 42)]

You can define pretty much any function you like and set it to automatically run whenever a ```CleverDict``` value is created or changed.  There's an example function built in to ```CleverDict``` which is illustrates this:

    >>> from cleverdict import my_example_save_function
    >>> CleverDict.save = my_example_save_function
    >>> x = CleverDict({'total':6, 'usergroup': "Knights of Ni"})
    Notional save to database: .total = 6 <class 'int'>
    Notional save to database: .usergroup = Knights of Ni <class 'str'>
    >>> x.life = 42
    Notional save to database: .life = 42 <class 'int'>


This example function appends all output to a file, which might be useful for debugging, auditing, or analysis over time:

    >>> with open("example.log","r") as file: log = file.read()
    >>> log.splitlines()
    ["Notional save to database: .age = 10 <class 'int'>",
    "Notional save to database: .total = 6 <class 'int'>",
    "Notional save to database: .usergroup = Knights of Ni <class 'str'>"]

**NB**: The ```.save()``` method is a *class* method, so changing ```CleverDict.save``` will apply the new ```.save()``` method to all previously created ```CleverDict``` objects as well.

If you want to specify different ```.save()``` behaviours for different instances, consider creating sublasses that inherit from ```CleverDict``` and set a different
```.save()``` function for each subclass.

    >>> class Type1(CleverDict): pass
    >>> Type1.save = my_save_function1
    >>> class Type2(CleverDict): pass
    >>> Type2.save = my_save_function2

When writing your own ```.save()``` function, it will need to accept three arguments:


    def your_function(self, name: str = "", value: any = ""):
        print("Ni!")


* **self**
* **name**: a valid Python ```.attribute``` name preferably, otherwise you'll only be able to access it using ```dictionary['key']``` notation later on.
* **value**: anything

## Contributing

We'd love to see Pull Requests (and relevant tests) from other contributors, particularly if you can help with one of the following items on our wish-list:

1. Although ```CleverDict``` does accept dictionary keys such as " " and "" and strings with characters not allowed in ```object.attribute``` names, it currently only handles the case where the first character is a number (it adds and underscore to the attribute name).  It would be great to think up and implement an elegant solution mapping 'problem' keys to attribute names.
2. It would be great if ```CleverDict``` behaviour could be easily 'grafted on' to existing classes using inheritance, without causing recursion or requiring a rewrite/overwrite of the original class.

For example if it were as easy as:

    >>> class MyDatetime(datetime.datetime, CleverDict):  pass
    >>> mdt = MyDatetime.now()
    >>> mdt.hour
    4
    >>> mdt['hour']
    4

## Credits
```CleverDict``` was developed jointly by Peter Fison, Ruud van der Ham, Loic Domaigne, and Rik Huygen who met on the friendly and excellent Pythonista Cafe forum (www.pythonistacafe.com).  Peter got the ball rolling after noticing a super-convenient, but not fully-fledged feature in Pandas that allows you to (mostly) use ```object.attribute``` syntax or ```dictionary['key']``` syntax interchangeably. Ruud, Loic and Rik then started swapping ideas for a hybrid  dictionary/data class based on ```UserDict``` and the magic of ```__getattr__``` and ```__setattr__```, and ```CleverDict``` (originally called ```attr_dict``` - which is 'taken' on PyPi already) was born.
