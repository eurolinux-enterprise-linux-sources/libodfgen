%global apiversion 0.1

Name: libodfgen
Version: 0.1.4
Release: 1%{?dist}
Summary: An ODF generator library

License: LGPLv2+ or MPLv2.0
URL: https://sourceforge.net/p/libwpd/wiki/libodfgen/
Source: http://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.xz

BuildRequires: boost-devel
BuildRequires: doxygen
BuildRequires: pkgconfig(librevenge-0.0)

%description
%{name} is a library for generating ODF documents. It is directly
pluggable into input filters based on librevenge. It is used in
libreoffice or calligra, for example.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation of %{name} API
BuildArch: noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%prep
%setup -q

%build
%configure --disable-silent-rules --disable-static --disable-werror
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.la
# we install API docs directly from build
rm -rf %{buildroot}/%{_docdir}/%{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING.* README NEWS
%{_libdir}/%{name}-%{apiversion}.so.*

%files devel
%doc ChangeLog
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc

%files doc
%doc COPYING.*
%doc docs/doxygen/html

%changelog
* Tue May 26 2015 David Tardon <dtardon@redhat.com> - 0.1.4-1
- Resolves: rhbz#1207758 rebase to 0.1.4

* Fri Apr 17 2015 David Tardon <dtardon@redhat.com> - 0.1.3-1
- Resolves: rhbz#1207758 rebase to 0.1.3

* Fri Aug 22 2014 David Tardon <dtardon@redhat.com> - 0.0.4-1
- Resolves: rhbz#1132072 rebase to 0.0.4

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.0.2-5
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.0.2-4
- Mass rebuild 2013-12-27

* Mon Sep 09 2013 David Tardon <dtardon@redhat.com> - 0.0.2-3
- do not build in C++11 mode

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 22 2013 David Tardon <dtardon@redhat.com> - 0.0.2-1
- new release

* Wed May 08 2013 David Tardon <dtardon@redhat.com> - 0.0.1-1
- new release

* Fri May 03 2013 David Tardon <dtardon@redhat.com> - 0.0.0-1
- initial import
