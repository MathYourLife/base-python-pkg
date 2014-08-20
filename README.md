# base-python-pkg

because I'm lazy and don't want to create this every time I start a new package

<!--- start_TOC -->

* [base-python-pkg](#base-python-pkg)
	* [Create A Package](#create-a-package)
	* [Commands](#commands)
		* [Bump the version](#bump-the-version)
		* [README Table of Contents](#readme-table-of-contents)

<!--- end_TOC -->

## Create A Package

```bash
NEWPKG="Quaternion"
mkdir $NEWPKG
git clone git@github.com:MathYourLife/base-python-pkg.git $NEWPKG
rm -rf $NEWPKG/.git
find $NEWPKG -type f -exec sed -i s/PackageName/$NEWPKG/g {} \;
mv $NEWPKG/src/{PackageName,$NEWPKG}
cd $NEWPKG
git init
git add .
git commit -a -m "initial commit"
git tag 0.0.0
```

## Commands

### Bump the version

```bash
make bump
```

Bump the git tag on `master` branch and update the `__version__` to match.
`make bump` will only be successful on the `master` branch and if
additional commits are present after the last tag.

### README Table of Contents

```bash
make toc
```

Longer `README.md` files can benefit from a Table of Contents.  The `#`
sections are parsed out and assembled into a hierarchical ToC in between
the tags

```html
<!--- start_TOC -->
<!--- end_TOC -->
```

Bug: picks up all lines that start with `#` including in code sections.