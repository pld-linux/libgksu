Summary:	libgksu library
Summary(pl):	Biblioteka libgksu
Name:		libgksu
Version:	1.2.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://people.debian.org/~kov/gksu/libgksu1.2/%{name}1.2-%{version}.tar.gz
# Source0-md5:	7a7449d649ea7012c958e4372a9db88a
URL:		http://www.nongnu.org/gksu/
BuildRequires:	glib2-devel
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgksu library.

%description -l pl
Biblioteka libgksu.

%package devel
Summary:	Header files for libgksu library
Summary(pl):	Pliki nag³ówkowe biblioteki libgksu
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel

%description devel
Header files for libgksu library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libgksu.

%package static
Summary:	Static libgksu library
Summary(pl):	Statyczna biblioteka libgksu
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgksu library.

%description static -l pl
Statyczna biblioteka libgksu.

%prep
%setup -q -n %{name}1.2-%{version}

%build
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}1.2

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}1.2.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/%{name}1.2
%attr(755,root,root) %{_libdir}/%{name}1.2/gksu-run-helper

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}*
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/%{name}*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
