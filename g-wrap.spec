
Summary:	A tool for exporting C libraries into Scheme interpreters
Name:		g-wrap
Version:	0.9.1
Release:	1
License:	GPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://ftp.gnucash.org/pub/g-wrap/%{name}-%{version}.tar.gz
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	guile

%description
This is a tool for specifying types, functions, and constants to
import into a Scheme interpreter, and for generating code (in C) to
interface these to the Guile and RScheme interpreters in particular.

%package devel
Summary:        headers for developing programs using g-wrap
Group:          Development/Libraries
Group(pl):      Programowanie/Biblioteki
Requires:       %{name} = %{version}

%description devel
headers for developing programs using g-wrap

%package static
Summary:        Static libraries for developing programs using g-wrap
Summary(pl):    Biblioteki statyczne g-wrap
Group:          Development/Libraries
Group(pl):      Programowanie/Biblioteki
Requires:       %{name}-devel = %{version}

%description static
Static libraries for developing programs using g-wrap.
 

%prep
%setup -q


%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

strip --strip-all $RPM_BUILD_ROOT%{_bindir}/g-scan
strip --strip-unneed $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/* NEWS README 

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
 
%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_bindir}/g-scan
%attr(755,root,root) %{_bindir}/g-wrap
%attr(755,root,root) %{_libexecdir}/*
%{_datadir}/guile/site/g-wrap
%{_datadir}/guile/site/g-wrap.scm

%files devel
%defattr(644,root,root,755)
%doc {NEWS,README}.gz
%attr(755,root,root) %{_bindir}/g-wrap-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*.h
%{_infodir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
