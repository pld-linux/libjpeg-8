Summary:     Library for handling different jpeg files.
Summary(de): Library zum Verarbeiten verschiedener jpeg-Dateien
Summary(fr): Bibliothèque pour gérer différents fichiers jpeg
Summary(tr): jpeg resimlerini iþleme kitaplýðý
Name:        libjpeg
Version:     6b
Release:     6
Copyright:   distributable
Group:       Libraries
Source0:     ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v%{version}.tar.gz
Buildroot:   /tmp/%{name}-%{version}-root

%description
This package is a library of functions that manipulate jpeg images, along
with simple clients for manipulating jpeg images.

%package devel
Summary:     headers and static libraries for developing programs using libjpeg
Summary(de): Header und statische Libraries zum Entwickeln von Programmen mit libjpeg
Summary(fr): Bibliothèques statiques et en-têtes pour développer avec libjpeg
Summary(tr): libjpeg için geliþtirme kitaplýklarý ve baþlýk dosyalarý
Group:       Development/Libraries
Requires:    %{name} = %{version}

%description devel
This package is all you need to develop programs that manipulate jpeg
images, including documentation.

%description -l de devel
Dieses Paket bietet alles, was Sie brauchen, um Programme zur Manipulation
von jpeg-Grafiken, einschließlich Dokumentation, zu entwickeln.

%description -l de
Dieses Paket ist eine Library mit Funktionen zur Manipulation von 
jpeg-Bildern, zusammen mit einfachen Clients zur Manipulation von jpeg-


%description -l fr devel
Ce package est tout ce dont vous avez besoin pour développer des
programmes manipulant des images jpg, et comprend la documentation.

%description -l fr
Bibliothèque de fonctions qui manipulent des images jpeg, et clients simples
pour manipuler de telles images.

%description -l tr devel
Bu paket, jpeg resimlerini iþleyen programlar geliþtirmeniz için gereken
baþlýk dosyalarýný, kitaplýklarý ve ilgili yardým belgelerini içerir.

%description -l tr
Bu paket, jpeg þekillerini iþlemek için kitaplýklar ve basit istemciler içerir.

%prep
%setup -q -n jpeg-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=$RPM_BUILD_ROOT/usr \
	--enable-shared --enable-static
make
LD_LIBRARY_PATH=$PWD make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{lib,include,bin,man/man1}
make install
make install-headers
make install-lib

strip $RPM_BUILD_ROOT/usr/{lib/lib*.so.*.*,bin/*}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755, root, root, 755)
/usr/lib/lib*.so.*.*
/usr/bin/*
%attr(644, root, man) /usr/man/*/*

%files devel
%defattr(644, root, root, 755)
/usr/lib/lib*.a
/usr/lib/lib*.so
/usr/include/*.h

%changelog
* Fri Jul 17 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [6b-6]
- added -q %setup parameter,
- added using %%{name} macro to Source an %setup,
- Buildroot changed to /tmp/%%{name}-%%{version}-root,
- added striping programs and shared libs,
- changed dependences for devel subpackage to
  "Requires: %%{name} = %%{version}",
- added %defattr and %attr macros in %files (allows building package from
  non-root account).

* Tue Jun 09 1998 Prospector System <bugs@redhat.com>
  [6b-5]
- translations modified for de

* Thu Jun 04 1998 Marc Ewing <marc@redhat.com>
- up to release 4
- remove patch that set (improper) soname - libjpeg now does it itself

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- fixed build on manhattan

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to version 6b

* Wed Oct 08 1997 Donnie Barnes <djb@redhat.com>
- new package to remove jpeg stuff from libgr and put in it's own package
