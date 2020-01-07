%global __strip /bin/true

Name:           panhunt
Version:        1.2.2
Release:        1%{?dist}
Summary:        PANhunt

License:        BSD 3 clause
URL:            https://github.com/btolab/PANhunt


%description
PANhunt is a tool that can be used to search drives for credit card numbers (PANs). This is useful for checking PCI DSS scope accuracy. It's designed to be a simple, standalone tool that can be run from a USB stick. PANhunt includes a python PST file parser.


%prep


%build


%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{_repodir}/dist/%{name} %{buildroot}%{_bindir}/%{name}

%files
%doc
%{_bindir}/%{name}

