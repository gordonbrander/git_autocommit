Autocommit
==========

Automatically commit to git whenever changes occur.

Use
---

```bash
autocommit [path/to/dir]
```

For example, say I want to check for changes in `design/comp:

```bash
$ autocommit /design/comp

Watching for changes every 10s. (ctl+c to stop)
[master ea42d34] [Auto] ios_app.psd
 1 file changed, 1 insertion(+)
 create mode 100644 ios_app.psd
```

You can set how often you want autocommit to check for changes with the `-s` flag:

```bash
autocommit -s 5 path/to/dir
```

Install
-------

Requirements:

- Python 2.x

Install from source via Pip:

```bash
git clone http://github.com/gordonbrander/git_autocommit.git
pip install -e git_autocommit
```

Or, just use it directly:

```bash
./git_autocommit.py path/to/dir
```