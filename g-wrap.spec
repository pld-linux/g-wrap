Summary:	A utility for automatically generating glue code to export C libraries to Guile Scheme and RScheme
Summary(pl):	Narz�dzie do eksportowania bibliotek C do interpreter�w Scheme
Summary(pt_BR):	Um utilit�rio para gera��o autom�tica de c�digo para exportar bibliotecas C para guile scheme e rscheme
Name:		g-wrap
Version:	1.1.10
Release:	1
Epoch:		2
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnucash.org/pub/g-wrap/source/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
BuildRequires:	guile-devel >= 1.4
BuildRequires:	texinfo
BuildRequires:	slib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a tool for specifying types, functions, and constants to
import into a Scheme interpreter, and for generating code (in C) to
interface these to the Guile and RScheme interpreters in particular.

%description -l pl
To jest narz�dzie do specyfikowania typ�w, funkcji i sta�ych dla
interpretera Scheme i generowania kodu (w C) do udost�pnienia ich dla
interpreter�w Guile i RScheme.

%description -l pt_BR
O g-wrap � uma ferramenta para especificar tipos, fun��es e constantes
para importa��o em um interpretador scheme e para gera��o de c�digo em
C para fazer a interface com os interpretadores guile e rscheme.

%package devel
Summary:	Headers for developing programs using g-wrap
Summary(pl):	Pliki nag��wkowe do rozwijnia program�w z u�yciem g-wrap
Summary(pt_BR):	Arquivos de inclus�o e bibliotecas para o g-wrap
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
headers for developing programs using g-wrap.

%description devel -l pl
Pliki nag��wkowe do rozwijania program�w z u�yciem g-wrap.

%description devel -l pt_BR
Arquivos de inclusao e bibliotecas para o g-wrap.

%package static
Summary:	Static libraries for developing programs using g-wrap
Summary(pl):	Biblioteki statyczne g-wrap
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com g-wrap
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries for developing programs using g-wrap.

%description static -l pl
Statyczne biblioteki g-wrap.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com a biblioteca g-wrap.

%prep
%setup -q
%patch0 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf NEWS README ChangeLog

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
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_datadir}/guile/g-wrapped/lib*.so.*
%attr(755,root,root) %{_datadir}/guile/g-wrapped/lib*.la
%{_datadir}/guile/g-wrap
%{_datadir}/guile/g-wrap.scm
%{_datadir}/guile/g-wrapped/*.scm

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/g-wrap-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_datadir}/guile/g-wrapped/lib*.so
%{_includedir}/*.h
%{_infodir}/*info*gz

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_datadir}/guile/g-wrapped/lib*.a
