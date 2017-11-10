Name:		franz
Version:	4.0.4
Release:	1%{?dist}
Summary:	Messaging app which combines chat and messaging services
License:	Proprietary
URL:		http://meetfranz.com/
Source0:	https://github.com/meetfranz/franz-app/releases/download/%{version}/Franz-linux-x64-%{version}.tgz

%description
Franz is a free messaging app / former Emperor of Austria and combines chat & messaging services into one application.
Franz currently supports Slack, WhatsApp, WeChat, HipChat, Facebook Messenger, Telegram, Google Hangouts, GroupMe, Skype and many more.

%prep
%setup -qn Franz-linux-x64-%{version}

%build


%install
mkdir -p %{buildroot}%{_bindir}
cp -p %{name} %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Wed Apr 26 2017 Jan Kalina <jkalina@redhat.com> - 0.8-1
- Initial Packaging
