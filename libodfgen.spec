%global apiversion 0.0

Name: libodfgen
Version: 0.0.2
Release: 5%{?dist}
Summary: An ODF generator library

Group: System Environment/Libraries
License: LGPLv2+ or MPLv2.0
URL: http://sourceforge.net/projects/libwpd/
Source: http://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.xz

BuildRequires: boost-devel
BuildRequires: libwpd-devel
BuildRequires: libwpg-devel

%description
%{name} is a library for generating ODF (text and vector drawing formats
only). It is directly pluggable into input filters based on
libwpd/libwpg. It is used in libreoffice, for example.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


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


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%doc COPYING.* README
%{_libdir}/%{name}-%{apiversion}.so.*


%files devel
%doc ChangeLog
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc


%changelog
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
