Name:		streameye
Version:	0.8
Release:	3%{?dist}
Summary:	Simple MJPEG streamer for Linux
License:	GPLv3
URL:		https://github.com/ccrisan/streameye
Source0:	https://github.com/ccrisan/streameye/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
Simple MJPEG streamer for Linux. It acts as an HTTP server and is capable
of serving multiple simultaneous clients.

It will feed the JPEGs read at input to all connected clients, in a MJPEG
stream. The JPEG frames at input may be delimited by a given separator.
In the absence of a separator, streamEye will auto-detect all JPEG frames.

%prep
%setup -qn %{name}-%{version}

%build
%make_build CFLAGS='%{optflags} -pthread -D_GNU_SOURCE' BINDIR=%{_bindir}

%install
mkdir -p %{buildroot}%{_bindir}
cp -p %{name} %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Tue Aug 22 2017 Jan Kalina <jkalina@redhat.com> - 0.8-3
- Preserve timestamps on copy, macros fix

* Fri Jun 2 2017 Jan Kalina <jkalina@redhat.com> - 0.8-2
- Correct using macros in spec

* Wed Apr 26 2017 Jan Kalina <jkalina@redhat.com> - 0.8-1
- Initial Packaging
