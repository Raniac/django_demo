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