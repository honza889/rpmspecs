%global commit0 5155493b18a384c0b28ff62cb5b61d11f4f6e1f8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gittag0 1.3.2
Name:		git-ftp		
Version:	1.3.2
Release:	1%{?dist}
Summary:	Git powered FTP client written as shell script
License:	GPLv3	
URL:		https://github.com/git-ftp
Source0:	https://github.com/%{name}/%{name}/archive/%{gittag0}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pandoc
BuildRequires:	man-db
Requires:	git
Requires:	curl	

%description
A shell script for pushing git tracked changed files to a 
remote host by FTP

%prep
%setup -qn %{name}-%{version}

%build
#Nothing to build

%install
make install-all DESTDIR=%{buildroot}%{_prefix} bindir=%{buildroot}%{_bindir} mandir=%{buildroot}%{_mandir}/man1

%check
# The testing environment expects to have Xampp installed 
# not applicable in this case

%files
%doc LICENSE README.md AUTHORS CHANGELOG.md
%{_bindir}/%{name}
%{_mandir}/man1/git-ftp.1*
%exclude %{_mandir}/man1/CACHEDIR.TAG.gz

%changelog
* Fri Feb 17 2017 Jan Kalina <jkalina@redhat.com> - 1.3.2-1
- Bump to the new version of upstream

* Fri Oct 09 2015 Eduardo Echeverria <echevemaster@gmail.com> - 1.0.2-1
- Bump to the new version of upstream

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>

* Tue Dec 30 2014 Eduardo Echeverria  <echevemaster@gmail.com> - 1.0.0-1
- Bump to the new version of upstream
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 30 2014 Eduardo Echeverria  <echevemaster@gmail.com> - 1.0.0-1
- Bump to the new version of upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 05 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 0.9.0-1
- Bump to the new version of upstream

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.84-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 0.84-1
- Initial Packaging
