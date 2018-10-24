Name:		whosaysthat
Version:	0.0.3
Release:	1%{?dist}
Summary:	This is an example project

Group:		Library
License:	GPLv3+
URL:		https://github.com/kushaldas/whosaysthat
Source0:	whosaysthat-0.0.3.tar.gz

BuildArch:      noarch
BuildRequires:	python3-setuptools
BuildRequires:	python3-devel

Requires:	python3-requests
Requires:       python3-cryptography

%description

We want to learn RPM packaing.

%prep
%setup -q


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install --skip-build --root %{buildroot}

%files
%doc README.md LICENSE
%{_bindir}/whatismyip
%{_bindir}/whoisthebest
%{python3_sitelib}/%{name}*
%{python3_sitelib}/mike*
%{_datadir}/%{name}


%changelog
* Wed Oct 24 2018 Kushal Das <kushal@freedom.press> - 0.0.3-1
- New update

* Wed Oct 24 2018 Kushal Das <kushal@freedom.press> - 0.0.2-1
- First release

