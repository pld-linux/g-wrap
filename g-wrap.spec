Summary:	A utility for automatically generating glue code to export C libraries to Guile Scheme and RScheme
Summary(pl.UTF-8):	Narzędzie do eksportowania bibliotek C do interpreterów Scheme
Summary(pt_BR.UTF-8):	Um utilitário para geração automática de código para exportar bibliotecas C para guile scheme e rscheme
Name:		g-wrap
Version:	1.9.15
Release:	3
Epoch:		2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://download.savannah.gnu.org/releases/g-wrap/%{name}-%{version}.tar.gz
# Source0-md5:	037d465a28782636a995cf0179f1d7ff
Patch0:		%{name}-info.patch
URL:		http://www.nongnu.org/g-wrap/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.12
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	guile-devel >= 5:2.0
BuildRequires:	libffi-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(libffi)
BuildRequires:	texinfo
Requires:	guile >= 5:2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a tool for specifying types, functions, and constants to
import into a Scheme interpreter, and for generating code (in C) to
interface these to the Guile and RScheme interpreters in particular.

%description -l pl.UTF-8
To jest narzędzie do specyfikowania typów, funkcji i stałych dla
interpretera Scheme i generowania kodu (w C) do udostępnienia ich dla
interpreterów Guile i RScheme.

%description -l pt_BR.UTF-8
O g-wrap é uma ferramenta para especificar tipos, funções e constantes
para importação em um interpretador scheme e para geração de código em
C para fazer a interface com os interpretadores guile e rscheme.

%package devel
Summary:	Headers for developing programs using g-wrap
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwijnia programów z użyciem g-wrap
Summary(pt_BR.UTF-8):	Arquivos de inclusão e bibliotecas para o g-wrap
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	guile-devel >= 5:2.0
Requires:	libffi-devel

%description devel
headers for developing programs using g-wrap.

%description devel -l pl.UTF-8
Pliki nagłówkowe do rozwijania programów z użyciem g-wrap.

%description devel -l pt_BR.UTF-8
Arquivos de inclusao e bibliotecas para o g-wrap.

%package static
Summary:	Static libraries for developing programs using g-wrap
Summary(pl.UTF-8):	Biblioteki statyczne g-wrap
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com g-wrap
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libraries for developing programs using g-wrap.

%description static -l pl.UTF-8
Statyczne biblioteki g-wrap.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com a biblioteca g-wrap.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-Werror \
	--disable-silent-rules

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgwrap-*.la
# dlopened modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/g-wrap/modules/libgw-*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/libgwrap-core-runtime.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgwrap-core-runtime.so.2
%attr(755,root,root) %{_libdir}/libgwrap-guile-runtime.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgwrap-guile-runtime.so.2
%dir %{_libdir}/g-wrap
%dir %{_libdir}/g-wrap/modules
%attr(755,root,root) %{_libdir}/g-wrap/modules/libgw-guile-gw-glib.so*
%attr(755,root,root) %{_libdir}/g-wrap/modules/libgw-guile-standard.so*
%{_datadir}/guile/site/g-wrap
%{_datadir}/guile/site/g-wrap.scm

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/g-wrap-config
%attr(755,root,root) %{_libdir}/libgwrap-core-runtime.so
%attr(755,root,root) %{_libdir}/libgwrap-guile-runtime.so
%{_includedir}/g-wrap
%{_includedir}/g-wrap-wct.h
%{_pkgconfigdir}/g-wrap-2.0-guile.pc
%{_aclocaldir}/g-wrap.m4
%{_mandir}/man1/g-wrap-config.1*
%{_infodir}/g-wrap.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgwrap-guile-runtime.a
%{_libdir}/libgwrap-core-runtime.a
