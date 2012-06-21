Name:		rhythmbox-ampache
Summary:	Ampache plugin for Rhythmbox
Version:	0.11
Release:	1%{?dist}
License:	GPLv2
Group:		Applications/Multimedia
URL:		http://code.google.com/p/rhythmbox-ampache/

Source:		http://rhythmbox-ampache.googlecode.com/files/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	rhythmbox

%description
Ampache plugin for Rhythmbox

%prep
%setup -q

#%build
#make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/rhythmbox/plugins/ampache
cp ampache/__init__.py ampache/[aA]mpache* %{buildroot}/%{_libdir}/rhythmbox/plugins/ampache

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc ampache/README
%{_libdir}/rhythmbox/plugins/ampache/*

%changelog
* Sat Oct 23 2010 Massimo Mund <massimo.mund@googlemail.com> 0.11-1
- Rhythmbox API changes

* Mon Apr 26 2010 Seva Epsteyn <seva@sevatech.com> 0.10-1
- Initial build
