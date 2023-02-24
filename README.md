# Starter app

So this is is more of a 'what-next' after reading or working-through Miguels Microblog Flask Mega Tutorial. I included his licence, but you should grab his licence if you plan on using this. If I take this app further it may reach a point where it looses the need to use that Licence. At this point it hasn't 2023-02-24.

see my blog at https://richard-porteous.github.io/2023/02/10/001-Flask.html


## Running on a server

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvii-deployment-on-linux

## Things to note should you choose to use the App factory in your own development.

in this app the global app will exist in two files (so far). The starter.py and the tests.py. 

If using python commands,  use app.app_context().push() after creating the app. If run using FLASK, Flask pushes an application context, which brings current_app and g (and other magic globals) to life. These 'globals' are specific to the thread handling the request.

Some things need to be passed app as a global when used - like async methods.
They can be passed current_app._get_current_object() instead of global 'app'.

Other things like cli need app as a global from the get go - like cli.
you can add a register method to its python file called register and register it in the starter.py file. I leave a dummy example.

<b>starter/cli.py</b>

    import os
    import click

    def register(app):
        @app.cli.group()
        def translate():
            """Translation and localization commands."""
            pass

and in <b>starter.py</b>

    ...
    app = create_app()
    cli.register(app)
    ...

## if you don't want the app-factory?

Use the no-app-factory branch ... it may be missing some files/features (or not), 2023-02-24 its missing this readme.

