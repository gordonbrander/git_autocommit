Autocommit
==========

Automatically commit to git whenever changes occur.

Autocommit automatically snapshots changes every 10s (at least). It does its best to create useful commit messages, so your git log is easy to browse through.

Autocommit is useful for any situation where you want to be lazy but still have
full versioning.

- Designers: no more `new-website.v5-B-final FINAL.psd`. You can have it all.
- Writers: [Markdown](https://ia.net/writer) <3 git
- Students: now your fancy [LaTeX](http://www.latex-project.org/) thesis docs have a full version history.


Use
---

```cli
autocommit [path/to/dir]
```

For example, say I want to check for changes in `design/psd`:

```cli
$ autocommit /design/psd

Watching for changes every 10s. (ctl+c to stop)
[master ea42d34] [Auto] ios_app.psd
 1 file changed, 1 insertion(+)
 create mode 100644 ios_app.psd
```

You can set how often you want autocommit to check for changes with the `-s` flag:

```cli
autocommit -s 5 path/to/dir
```


Install
-------

Requirements:

- Python 2.x

Install from source via Pip:

```cli
git clone http://github.com/gordonbrander/git_autocommit.git
pip install -e git_autocommit
```

Or, just use it directly:

```cli
./git_autocommit.py path/to/dir
```