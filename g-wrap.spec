Summary:	A utility for automatically generating glue code to export C libraries to Guile Scheme and RScheme
Summary(pl):	Narz�dzie do eksportowania bibliotek C do interpreter�w Scheme
Summary(pt_BR):	Um utilit�rio para gera��o autom�tica de c�digo para exportar bibliotecas C para guile scheme e rscheme
Name:		g-wrap
Version:	1.9.7
Release:	1
Epoch:		2
License:	LGPL
Group:		Libraries
Source0:	http://download.savannah.gnu.org/releases/g-wrap/%{name}-%{version}.tar.gz
# Source0-md5:	4e980fd3f464d53ecee12184569c32bf
Patch0:		%{name}-info.patch
Patch1:		%{name}-glib2.patch
URL:		http://www.nongnu.org/g-wrap/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	guile-devel >= 5:1.8
BuildRequires:	libffi-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	texinfo
Requires:	guile > 5:1.8
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
Requires:	guile-devel >= 5:1.8

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

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/g-wrap/modules/libgw-*.{a,la}

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
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/libgwrap-core-runtime.so.*.*.*
%attr(755,root,root) %{_libdir}/libgwrap-guile-runtime.so.*.*.*
%dir %{_libdir}/g-wrap
%dir %{_libdir}/g-wrap/modules
%attr(755,root,root) %{_libdir}/g-wrap/modules/libgw-guile-gw-glib.so*
%attr(755,root,root) %{_libdir}/g-wrap/modules/libgw-guile-standard.so*
%dir %{_datadir}/guile
%dir %{_datadir}/guile/site
%{_datadir}/guile/site/g-wrap
%dir %{_datadir}/guile/site/srfi
# srfi-34.scm already in recent guile
%{_datadir}/guile/site/srfi/srfi-35.scm
%{_datadir}/guile/site/g-wrap.scm
%{_infodir}/g-wrap.info*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/g-wrap-config
%attr(755,root,root) %{_libdir}/libgwrap-core-runtime.so
%attr(755,root,root) %{_libdir}/libgwrap-guile-runtime.so
%{_libdir}/libgwrap-core-runtime.la
%{_libdir}/libgwrap-guile-runtime.la
%{_includedir}/g-wrap
%{_includedir}/g-wrap*.h
%{_pkgconfigdir}/g-wrap-2.0-guile.pc
%{_aclocaldir}/g-wrap.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libgwrap-guile-runtime.a
%{_libdir}/libgwrap-core-runtime.a
