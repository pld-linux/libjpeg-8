Summary:	Library for handling different jpeg files
Summary(de):	Library zum Verarbeiten verschiedener jpeg-Dateien
Summary(fr):	Bibliothèque pour gérer différents fichiers jpeg
Summary(pl):	Biblioteki do manipulacji plikami w ró¿nych formatach jpeg
Summary(tr):	jpeg resimlerini iþleme kitaplýðý
Name:		libjpeg
Version:	6b
Release:	17
License:	distributable
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v%{version}.tar.gz
URL:		http://www.ijg.org/
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-arm.patch
Patch2:		%{name}-include.patch
Patch3:		%{name}-c++.patch
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libjpeg package contains a library of functions for manipulating
JPEG images.

%description -l de
Dieses Paket ist eine Library mit Funktionen zur Manipulation von
jpeg-Bildern, zusammen mit einfachen Clients zur Manipulation von
jpeg.

%description -l fr
Bibliothèque de fonctions qui manipulent des images jpeg, et clients
simples pour manipuler de telles images.

%description -l pl
Ten pakiet zawiera bibliotekê funkcji do manipulacji plikami jpeg.

%description -l tr
Bu paket, jpeg þekillerini iþlemek için kitaplýklar ve basit
istemciler içerir.

%package devel
Summary:	headers for developing programs using libjpeg
Summary(de):	Header und statische Libraries zum Entwickeln von Programmen mit libjpeg
Summary(fr):	Bibliothèques statiques et en-têtes pour développer avec libjpeg
Summary(pl):	Pliki nag³ówkowe libjpeg
Summary(tr):	libjpeg için geliþtirme kitaplýklarý ve baþlýk dosyalarý
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The libjpeg-devel package includes the header files and static
libraries necessary for developing programs which will manipulate JPEG
files using the libjpeg library.

If you are going to develop programs which will manipulate JPEG
images, you should install libjpeg-devel. You'll also need to have the
libjpeg package installed.

%description -l de devel
Dieses Paket bietet alles, was Sie brauchen, um Programme zur
Manipulation von jpeg-Grafiken, einschließlich Dokumentation, zu
entwickeln.

%description -l fr devel
Ce package est tout ce dont vous avez besoin pour développer des
programmes manipulant des images jpg, et comprend la documentation.

%description -l pl devel
Ten pakiet pozwoli Ci na programowanie z wykorzystniem formatu jpeg.
Zawiera tak¿e dokumentacjê.

%description -l tr devel
Bu paket, jpeg resimlerini iþleyen programlar geliþtirmeniz için
gereken baþlýk dosyalarýný, kitaplýklarý ve ilgili yardým belgelerini
içerir.

%package progs
Summary:	Simple clients for manipulating jpeg images
Summary(de):	Einfachen Clients zur Manipulation von jpeg
Summary(fr):	Clients simples pour manipuler de telles images
Summary(pl):	Kilka prostych programów do manipulowania na plikach jpeg
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description progs
Simple clients for manipulating jpeg images. Libjpeg client programs
include cjpeg, djpeg, jpegtran, rdjpgcom and wrjpgcom. Djpeg
decompresses a JPEG file into a regular image file. Jpegtran can
perform various useful transformations on JPEG files. Rdjpgcom
displays any text comments included in a JPEG file. Wrjpgcom inserts
text comments into a JPEG file.

%description progs -l de
Einfachen Clients zur Manipulation von jpeg.

%description progs -l fr
Clients simples pour manipuler de telles images.

%description progs -l pl
Kilka prostych programów do manipulowania na plikach jpeg.

%package static
Summary:	Static libraries for developing programs using libjpeg
Summary(pl):	Biblioteki statyczne libjpeg
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries for developing programs using libjpeg.

%description -l pl static
Statyczna bibliteka libjpeg.

%prep
%setup  -q -n jpeg-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cp -f %{_datadir}/libtool/config.sub .
%configure \
	--enable-shared \
	--enable-static

%{__make}
LD_PRELOAD=$PWD/.libs/%{name}.so make test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_bindir},%{_mandir}/man1}

%{__make} DESTDIR=$RPM_BUILD_ROOT \
	install install-headers install-lib

install jversion.h $RPM_BUILD_ROOT%{_includedir}

gzip -9nf {libjpeg,structure}.doc

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {libjpeg,structure}.doc.gz

%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*.h

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
