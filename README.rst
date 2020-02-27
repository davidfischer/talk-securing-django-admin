Securing the Django Admin
=========================

This talk is made up of slides and code samples.
If you just want to download the slides,
you can do that in the "Releases" section of the repository.

.. TODO

    You can also watch a video of this talk on `YouTube <>`_.


Other talks in this series
--------------------------

* Optimizing the Django Admin (`slides <https://github.com/davidfischer/talk-optimizing-django-admin>`_, `video <https://youtu.be/F60CSzpe-As>`_)
* Customizing the Django Admin (`slides <https://github.com/davidfischer/talk-customizing-django-admin>`_, `video <https://www.youtube.com/watch?v=OtZhbtjaYBY>`_)
* Django Admin Add-Ons & Extensions (not yet given)


Building the slides
-------------------

You will need to source the requirements.txt file.
There are source code examples in the talk and pygments is required to syntax highlight them.
You will also need LaTeXPDF.

::

    % cd slides
    % make


Running the code samples
------------------------

The blog application code sample used in the talk is available under ``code-sample``.
You will need to source the requirements.txt file to run it.

::

    % cd code-sample
    % ./manage.py migrate           # Creates a local sqlite database with some blog data
    % ./manage.py createsuperuser   # Creates a user account for your local django admin
    % ./manage.py runserver

Then open your browser to http://localhost:8000
and login with the account created above with ``createsuperuser``.

The interesting bits of code are in ``blog/models.py`` and ``blog/admin.py``.
