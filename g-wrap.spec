Summary:	A utility for automatically generating glue code to export C libraries to Guile Scheme and RScheme
Summary(pl):	Narz�dzie do eksportowania bibliotek C do interpreter�w Scheme
Summary(pt_BR):	Um utilit�rio para gera��o autom�tica de c�digo para exportar bibliotecas C para guile scheme e rscheme
Name:		g-wrap
Version:	1.3.4
Release:	5
Epoch:		2
License:	LGPL
Group:		Libraries
Source0:	http://www.gnucash.org/pub/g-wrap/source/%{name}-%{version}.tar.gz
# Source0-md5:	bf29b8b563cc27d9f7fd90a6243653aa
Patch0:		%{name}-info.patch
Patch1:		%{name}-ac_am_cflags.patch
Patch2:		%{name}-am18.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel >= 1.0
BuildRequires:	guile-devel >= 1.4.1
# guile-gtk for gtk wrappers
BuildRequires:	libtool
BuildRequires:	slib
BuildRequires:	texinfo
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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	guile-devel >= 1.4.1

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
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libraries for developing programs using g-wrap.

%description static -l pl
Statyczne biblioteki g-wrap.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com a biblioteca g-wrap.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# modules
rm -f $RPM_BUILD_ROOT%{_libdir}/libgw-*.a

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
# libs
%attr(755,root,root) %{_libdir}/libgwrap-glib.so.*.*.*
%attr(755,root,root) %{_libdir}/libgwrap-wct.so.*.*.*
# modules (lt)dlopened by .so OR .la
%attr(755,root,root) %{_libdir}/libgw-glib.so.*.*.*
#%attr(755,root,root) %{_libdir}/libgw-gtk.so.*.*.*
%attr(755,root,root) %{_libdir}/libgw-standard.so.*.*.*
%attr(755,root,root) %{_libdir}/libgw-wct.so.*.*.*
%attr(755,root,root) %{_libdir}/libgw-glib.so
#%attr(755,root,root) %{_libdir}/libgw-gtk.so
%attr(755,root,root) %{_libdir}/libgw-standard.so
%attr(755,root,root) %{_libdir}/libgw-wct.so
%{_libdir}/libgw-glib.la
#%{_libdir}/libgw-gtk.la
%{_libdir}/libgw-standard.la
%{_libdir}/libgw-wct.la
%{_datadir}/guile/g-wrap
%{_datadir}/guile/g-wrap.scm

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/g-wrap-config
%attr(755,root,root) %{_libdir}/libgwrap-glib.so
%attr(755,root,root) %{_libdir}/libgwrap-wct.so
%{_libdir}/libgwrap-glib.la
%{_libdir}/libgwrap-wct.la
%{_includedir}/g-wrap
%{_infodir}/*.info*
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libgwrap-glib.a
%{_libdir}/libgwrap-wct.a
