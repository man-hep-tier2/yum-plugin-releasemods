# yum-plugin-releasemods
Yum plugin that can prevent specific release packages to install any repo files.

## Building the RPM as non-root

The following instructions have been tested on SL6 and CentOS7:
* Download a tagged release (tar.gz) into `$HOME/rpmbuild/SOURCES`, e.g.
```bash
sdir=$HOME/rpmbuild/SOURCES
[ -d $sdir ] || mkdir -p $sdir
v=1.1
curl -Lo $sdir/yum-plugin-releasemods-${v}.tar.gz https://github.com/man-hep-tier2/yum-plugin-releasemods/archive/v${v}.tar.gz
```
* Extract the spec file from the archive, e.g.
```bash
tar xvf $sdir/yum-plugin-releasemods-${v}.tar.gz yum-plugin-releasemods-${v}/yum-plugin-releasemods.spec
```
* Run rpmbuild on the spec file, e.g.
```bash
rpmbuild -ba yum-plugin-releasemods-${v}/yum-plugin-releasemods.spec
```

The above example will create a binary rpm (in `$HOME/rpmbuild/RPMS/noarch`) and a source rpm (in `$HOME/rpmbuild/SRPMS`).

