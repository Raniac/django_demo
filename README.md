# django_demo
Refer to [this site](https://segmentfault.com/a/1190000009878124) for the instructions to build a django environment.

Set up the django and selenium environment according to *Test-Driven Development with Python*. If encountered an error like below,
```bash
File "/home/bennyray/Projects/django_demo/env/lib/python3.7/site-packages/django/contrib/admin/widgets.py", line 152
    '%s=%s' % (k, v) for k, v in params.items(),
    ^
SyntaxError: Generator expression must be parenthesized
``` 
refer to [this site](http://blog.51cto.com/13859849/2318942) for solution, basically just open the mentioned file and remove the comma at the end of line 152.

Make sure to look into **netstat** commands.

To empty the git repository, use the command,
```bash
$ rm -rf .git
$ git init .
```
Apps are a good way to keep code organized, started by,
```bash
$ python manage.py startapp web
```
consists of a number of placeholder files for things like models, views, and tests.

Before doing any refactoring, always do a commit.

To let Git notice that some files are moved, use **git mv** command.

If something strange is going on with the FT's, it's always worth trying to upgrade Selenium.