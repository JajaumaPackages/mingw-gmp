%{?mingw_package_header}

Name:       mingw-gmp
Version:    6.1.1
Release:    2%{?dist}

Summary:    Cross-compiled GNU arbitrary precision library
License:    LGPLv3+ or GPLv2+
Group:      System Environment/Libraries
URL:        http://gmplib.org/
Source0:    ftp://ftp.gnu.org/pub/gnu/gmp/gmp-%{version}.tar.xz
Source1:    ftp://ftp.gnu.org/pub/gnu/gmp/gmp-%{version}.tar.xz.sig

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++

BuildRequires:  libtool


%description
The gmp package contains GNU MP, a library for arbitrary precision
arithmetic, signed integers operations, rational numbers and floating
point numbers. GNU MP is designed for speed, for both small and very
large operands. GNU MP is fast because it uses fullwords as the basic
arithmetic type, it uses fast algorithms, it carefully optimizes
assembly code for many CPUs' most common inner loops, and it generally
emphasizes speed over simplicity/elegance in its operations.

Install the gmp package if you need a fast arbitrary precision
library.


# Mingw32
%package -n mingw32-gmp
Summary: Cross-compiled GNU arbitrary precision library


%description -n mingw32-gmp
The gmp package contains GNU MP, a library for arbitrary precision
arithmetic, signed integers operations, rational numbers and floating
point numbers. GNU MP is designed for speed, for both small and very
large operands. GNU MP is fast because it uses fullwords as the basic
arithmetic type, it uses fast algorithms, it carefully optimizes
assembly code for many CPUs' most common inner loops, and it generally
emphasizes speed over simplicity/elegance in its operations.

Install the gmp package if you need a fast arbitrary precision
library.


# Mingw64
%package -n mingw64-gmp
Summary: Cross-compiled GNU arbitrary precision library


%description -n mingw64-gmp
The gmp package contains GNU MP, a library for arbitrary precision
arithmetic, signed integers operations, rational numbers and floating
point numbers. GNU MP is designed for speed, for both small and very
large operands. GNU MP is fast because it uses fullwords as the basic
arithmetic type, it uses fast algorithms, it carefully optimizes
assembly code for many CPUs' most common inner loops, and it generally
emphasizes speed over simplicity/elegance in its operations.

Install the gmp package if you need a fast arbitrary precision
library.


%?mingw_debug_package


%prep
%setup -q -n gmp-%{version}


%build
%mingw_configure \
    --enable-shared \
    --disable-static \
    --enable-mpbsd \
    --enable-cxx
export LD_LIBRARY_PATH=`pwd`/.libs
%mingw_make %{?_smp_mflags}


%install
export LD_LIBRARY_PATH=`pwd`/.libs
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/lib{gmp,mp,gmpxx}.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/lib{gmp,mp,gmpxx}.la

# Remove documentation which duplicates that found in the native package.
rm -r $RPM_BUILD_ROOT/%{mingw32_prefix}/share
rm -r $RPM_BUILD_ROOT/%{mingw64_prefix}/share


# Win32
%files -n mingw32-gmp
%license COPYING COPYING.LESSERv3 COPYINGv2 COPYINGv3
%doc NEWS README
%{mingw32_bindir}/libgmp-10.dll
%{mingw32_bindir}/libgmpxx-4.dll
%{mingw32_libdir}/libgmp.dll.a
%{mingw32_libdir}/libgmpxx.dll.a
%{mingw32_includedir}/gmp.h
%{mingw32_includedir}/gmpxx.h


# Win64
%files -n mingw64-gmp
%license COPYING COPYING.LESSERv3 COPYINGv2 COPYINGv3
%doc NEWS README
%{mingw64_bindir}/libgmp-10.dll
%{mingw64_bindir}/libgmpxx-4.dll
%{mingw64_libdir}/libgmp.dll.a
%{mingw64_libdir}/libgmpxx.dll.a
%{mingw64_includedir}/gmp.h
%{mingw64_includedir}/gmpxx.h


%changelog
* Thu Feb 02 2017 Jajauma's Packages <jajauma@yandex.ru> - 6.1.1-2
- Rebuild with GCC 5.4.0

* Tue Oct 04 2016 Michael Cronenworth <mike@cchtml.com> - 6.1.1-1
- New upstream release.

* Tue Jun 07 2016 Michael Cronenworth <mike@cchtml.com> - 6.1.0-1
- New upstream release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Michael Cronenworth <mike@cchtml.com> - 6.0.0-1
- New upstream release.

* Tue Jan 07 2014 Michael Cronenworth <mike@cchtml.com> - 5.1.3-1
- New upstream release.

* Sun Sep 22 2013 Michael Cronenworth <mike@cchtml.com> - 5.1.2-1
- New upstream release.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 15 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.1.1-2
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Thu May 09 2013 Michael Cronenworth <mike@cchtml.com> - 5.1.1-1
- New upstream release.

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.5-2
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Mon Sep 03 2012 Michael Cronenworth <mike@cchtml.com> - 5.0.5-1
- New upstream release.

* Wed Aug 29 2012 Michael Cronenworth <mike@cchtml.com> - 5.0.2-4
- Don't ship include wrappers

* Wed Aug 29 2012 Michael Cronenworth <mike@cchtml.com> - 5.0.2-3
- Don't autoreconf

* Sun Aug 26 2012 Michael Cronenworth <mike@cchtml.com> - 5.0.2-2
- Add BR for mingw-gcc-c++
- Install gmp source headers

* Mon Jun 18 2012 Michael Cronenworth <mike@cchtml.com> - 5.0.2-1
- Initial RPM package
