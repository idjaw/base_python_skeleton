base_python_skeleton
====================

Basic Structure For a Python Project

The only assumption here is that you have virtualenv already installed.

If you don't, simply open up a shell and run

```
pip install virtualenv
```

Install and activate your virtualenv like this:

```
virtualenv venv
source venv/bin/activate
```

You can add whatever modules you night need to your setup-requires and run:

```
pip install -r setup-requires
```

Enjoy!

#### TO DO
Want to add a mechanism to enable and configure the virtualenv upon running the application to remove the need to do any manual steps around enabling the virtualenv and installing any required modules within your venv
