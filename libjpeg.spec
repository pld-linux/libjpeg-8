Summary:	Library for handling different jpeg files.
Summary(de):	Library zum Verarbeiten verschiedener jpeg-Dateien
Summary(fr):	Bibliothèque pour gérer différents fichiers jpeg
Summary(pl):	Biblioteki do manipulacji plikami w ró¿nych formatach jpeg
Summary(tr):	jpeg resimlerini iþleme kitaplýðý
Name:		libjpeg
Version:	6b
Release:	11
Copyright:	distributable
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v%{version}.tar.gz
Buildroot:	/tmp/%{name}-%{version}-root

%description
This package is a library of functions that manipulate jpeg images

%description -l de
Dieses Paket ist eine Library mit Funktionen zur Manipulation von 
jpeg-Bildern.

%description -l fr
Bibliothèque de fonctions qui manipulent des images jpeg

%description -l pl
Ten pakiet zawiera bibliotekê funkcji do manipulacji plikami jpeg.

%description -l tr
Bu paket, jpeg þekillerini iþlemek için kitaplýklar ve basit istemciler içerir.

%package devel
Summary:	headers for developing programs using libjpeg
Summary(de):	Header und statische Libraries zum Entwickeln von Programmen mit libjpeg
Summary(fr):	Bibliothèques statiques et en-têtes pour développer avec libjpeg
Summary(tr):	libjpeg için geliþtirme kitaplýklarý ve baþlýk dosyalarý
Summary(pl):	Pliki nag³ówkowe libjpeg
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package is all you need to develop programs that manipulate jpeg
images, including documentation.

%description -l de devel
Dieses Paket bietet alles, was Sie brauchen, um Programme zur Manipulation
von jpeg-Grafiken, einschließlich Dokumentation, zu entwickeln.

%description -l fr devel
Ce package est tout ce dont vous avez besoin pour développer des
programmes manipulant des images jpg, et comprend la documentation.

%description -l pl devel
Ten pakiet pozwoli Ci na programowanie z wykorzystniem formatu jpeg.
Zawiera tak¿e dokumentacjê.

%description -l tr devel
Bu paket, jpeg resimlerini iþleyen programlar geliþtirmeniz için gereken
baþlýk dosyalarýný, kitaplýklarý ve ilgili yardým belgelerini içerir.

%package progs
Summary:	Simple clients for manipulating jpeg images
Summary(de):	Einfachen Clients zur Manipulation von jpeg
Summary(fr):	Clients simples pour manipuler de telles images
Summary(pl):	Kilka prostych programów do manipulowania na plikach jpeg
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description progs
Simple clients for manipulating jpeg images.

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
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries for developing programs using libjpeg

%description -l pl static
Statyczna bibliteka libjpeg.

%prep
%setup -q -n jpeg-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=$RPM_BUILD_ROOT%{_prefix} \
	--enable-shared \
	--enable-static

make
LD_LIBRARY_PATH=$PWD make test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_bindir},%{_mandir}/man1}

make install mandir=$RPM_BUILD_ROOT%{_mandir}/man1
make install-headers
make install-lib

strip $RPM_BUILD_ROOT/{%{_libdir}/lib*so.*.*,%{_bindir}/*}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	{libjpeg,structure}.doc

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
%{_includedir}/*.h

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Thu May 20 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [6b-11]
- spec based on RH spec,
- pl translation by Wojtek ¦lusarczyk <wojtek@shadow.eu.org>,
- spec rewritten by Wojtek ¦lusarczyk <wojtek@shadow.eu.org> and me.
