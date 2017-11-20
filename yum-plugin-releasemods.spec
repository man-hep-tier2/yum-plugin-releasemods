Summary: Yum plugin that removes the yum repo packages that are installed by release files.
Name: yum-plugin-releasemods
Version: 1.1
Release: 2
BuildArch: noarch
Group: System
License: ASL 2.0
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-buildroot
#Requires: 
%description
The plugin checks for yum repository files that were installed by release packages
(such as epel-release) and removes them. This ensures that they don't interfere with
local mirrors of those repositories.

%prep
%setup

%install
rm -rf %{buildroot}
install -d %{buildroot}/usr/lib/yum-plugins
install -d %{buildroot}/etc/yum/pluginconf.d
install -m 0644 src/releasemods.py %{buildroot}/usr/lib/yum-plugins/releasemods.py
install -m 0644 src/releasemods.conf %{buildroot}/etc/yum/pluginconf.d/releasemods.conf

%postun
rm -f /usr/lib/yum-plugins/releasemods.py[co]

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/lib/yum-plugins/releasemods.py*
/etc/yum/pluginconf.d/releasemods.conf

%changelog
* Mon Nov 20 2017 Robert Frank <robert.frank@manchester.ac.uk>
- fix source path in spec file
- fix files section
* Fri Apr 24 2015 Robert Frank <robert.frank@manchester.ac.uk>
- added foreman-release to configuration
* Tue Nov 18 2014 Robert Frank <robert.frank@manchester.ac.uk>
- added wlcg-repo to configuration
* Fri Dec 6 2013 Robert Frank <robert.frank@manchester.ac.uk>
- added internet2-repo to configuration
* Thu Dec 5 2013 Robert Frank <robert.frank@manchester.ac.uk>
- added centos-release to configuration
* Thu Jun 27 2013 Robert Frank <robert.frank@manchester.ac.uk>
- added configuration option to delete specific files for each release package
- improved error checking
- added sl6x.repo file as a file to be deleted for sl-release to releasemods.conf
* Fri Jun 7 2013 Robert Frank <robert.frank@manchester.ac.uk>
- added puppetlabs-release to releasemods.conf
* Fri Sep 21 2012 Robert Frank <robert.frank@manchester.ac.uk>
- first version
