Summary:	A utility for automatically generating glue code to export C libraries to Guile Scheme and RScheme
Summary(pl):	Narzêdzie do eksportowania bibliotek C do interpreterów Scheme
Summary(pt_BR):	Um utilitário para geração automática de código para exportar bibliotecas C para guile scheme e rscheme
Name:		g-wrap
Version:	1.3.4
Release:	2
Epoch:		2
License:	GPL
Group:		Libraries
Source0:	http://www.gnucash.org/pub/g-wrap/source/%{name}-%{version}.tar.gz
# Source0-md5:	bf29b8b563cc27d9f7fd90a6243653aa
Patch0:		%{name}-info.patch
#Patch1:		%{name}-ac_am_cflags.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	guile-devel >= 1.4.1
BuildRequires:	libtool
BuildRequires:	slib
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a tool for specifying types, functions, and constants to
import into a Scheme interpreter, and for generating code (in C) to
interface these to the Guile and RScheme interpreters in particular.

%description -l pl
To jest narzêdzie do specyfikowania typów, funkcji i sta³ych dla
interpretera Scheme i generowania kodu (w C) do udostêpnienia ich dla
interpreterów Guile i RScheme.

%description -l pt_BR
O g-wrap é uma ferramenta para especificar tipos, funções e constantes
para importação em um interpretador scheme e para geração de código em
C para fazer a interface com os interpretadores guile e rscheme.

%package devel
Summary:	Headers for developing programs using g-wrap
Summary(pl):	Pliki nag³ówkowe do rozwijnia programów z u¿yciem g-wrap
Summary(pt_BR):	Arquivos de inclusão e bibliotecas para o g-wrap
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description devel
headers for developing programs using g-wrap.

%description devel -l pl
Pliki nag³ówkowe do rozwijania programów z u¿yciem g-wrap.

%description devel -l pt_BR
Arquivos de inclusao e bibliotecas para o g-wrap.

%package static
Summary:	Static libraries for developing programs using g-wrap
Summary(pl):	Biblioteki statyczne g-wrap
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com g-wrap
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
Static libraries for developing programs using g-wrap.

%description static -l pl
Statyczne biblioteki g-wrap.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com a biblioteca g-wrap.

%prep
%setup -q
%patch0 -p1
#%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%doc NEWS README ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_libdir}/lib*.la
#%attr(755,root,root) %{_datadir}/guile/g-wrapped/lib*.so.*
#%{_datadir}/guile/g-wrapped/lib*.la
%{_datadir}/guile/g-wrap
%{_datadir}/guile/g-wrap.scm
#%{_datadir}/guile/g-wrapped/*.scm

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/g-wrap-config
%attr(755,root,root) %{_libdir}/lib*.so
#%attr(755,root,root) %{_datadir}/guile/g-wrapped/lib*.so
%{_includedir}/g-wrap
%{_infodir}/*info*
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
#%{_datadir}/guile/g-wrapped/lib*.a
