# TODO
# - ftp://ftp.graphicsmagick.org/pub/GraphicsMagick/delegates/ljpeg-6b.tar.gz
# NOTE: it changes ABI! either make it work without ABI breakage, or build
#       second libjpeg (with lossless support) with different name/soname
#
# Conditional build:
%bcond_with	crop	# "apply" crop pseudo-patch
#
Summary:	Library for handling different jpeg files
Summary(de.UTF-8):   Library zum Verarbeiten verschiedener jpeg-Dateien
Summary(es.UTF-8):   Biblioteca para manipulación de diferentes archivos jpegs
Summary(fr.UTF-8):   Bibliothèque pour gérer différents fichiers jpeg
Summary(pl.UTF-8):   Biblioteka do manipulacji plikami w formacie jpeg
Summary(pt_BR.UTF-8):   Biblioteca para manipulação de diferentes arquivos jpegs
Summary(ru.UTF-8):   Библиотека для обработки различных jpeg-файлов
Summary(tr.UTF-8):   jpeg resimlerini işleme kitaplığı
Summary(uk.UTF-8):   Бібліотека для обробки різноманітних jpeg-файлів
Name:		libjpeg
Version:	6b
Release:	27
License:	distributable
Group:		Libraries
Source0:	ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v%{version}.tar.gz
# Source0-md5:	dbd5f3b47ed13132f04c685d608a7547
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	d6342c015a489de275ada637a77dc2b0
Source2:	http://sylvana.net/jpegcrop/croppatch.tar.gz
# Source2-md5:	45d76e4226232439308e2129b64c4ea1
URL:		http://www.ijg.org/
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-arm.patch
Patch2:		%{name}-include.patch
Patch3:		%{name}-c++.patch
Patch4:		%{name}-libtool.patch
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libjpeg package contains a library of functions for manipulating
JPEG images.

%description -l de.UTF-8
Dieses Paket ist eine Library mit Funktionen zur Manipulation von
jpeg-Bildern, zusammen mit einfachen Clients zur Manipulation von
jpeg.

%description -l es.UTF-8
Este paquete contiene una biblioteca de funciones y programas
sencillos que manipulan imágenes jpeg.

%description -l fr.UTF-8
Bibliothèque de fonctions qui manipulent des images jpeg, et clients
simples pour manipuler de telles images.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę funkcji do manipulacji plikami jpeg.

%description -l pt_BR.UTF-8
Este pacote contém uma biblioteca de funções e programas simples que
manipulam imagens jpeg.

%description -l ru.UTF-8
Библиотека функций для обработки jpeg-изображений и простые клиенты
для такой обработки.

%description -l tr.UTF-8
Bu paket, jpeg şekillerini işlemek için kitaplıklar ve basit
istemciler içerir.

%description -l uk.UTF-8
Бібліотека функцій для обробки jpeg-зображень та прості клієнти для
такої обробки.

%package devel
Summary:	Headers for developing programs using libjpeg
Summary(de.UTF-8):   Header und statische Libraries zum Entwickeln von Programmen mit libjpeg
Summary(es.UTF-8):   Archivos de inclusión y bibliotecas para desarrollar programas usando libjpeg
Summary(fr.UTF-8):   Bibliothèques statiques et en-têtes pour développer avec libjpeg
Summary(pl.UTF-8):   Pliki nagłówkowe libjpeg
Summary(pt_BR.UTF-8):   Arquivos de inclusão e bibliotecas para desenvolver programas usando libjpeg
Summary(ru.UTF-8):   Хедеры и библиотека для разработки программ, использующих libjpeg
Summary(tr.UTF-8):   libjpeg için geliştirme kitaplıkları ve başlık dosyaları
Summary(uk.UTF-8):   Хедери та бібліотека для розробки програм, що використовують libjpeg
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The libjpeg-devel package includes the header files and static
libraries necessary for developing programs which will manipulate JPEG
files using the libjpeg library.

If you are going to develop programs which will manipulate JPEG
images, you should install libjpeg-devel. You'll also need to have the
libjpeg package installed.

%description devel -l de.UTF-8
Dieses Paket bietet alles, was Sie brauchen, um Programme zur
Manipulation von jpeg-Grafiken, einschließlich Dokumentation, zu
entwickeln.

%description devel -l es.UTF-8
Este paquete es todo lo que necesitas para desarrollar programas que
manipulen imágenes jpeg, incluso documentación.

%description devel -l fr.UTF-8
Ce package est tout ce dont vous avez besoin pour développer des
programmes manipulant des images jpg, et comprend la documentation.

%description devel -l pl.UTF-8
Ten pakiet pozwoli Ci na programowanie z wykorzystaniem formatu jpeg.
Zawiera także dokumentację.

%description devel -l pt_BR.UTF-8
Este pacote é tudo que você precisa para desenvolver programas que
manipulam imagens jpeg, incluindo documentação.

%description devel -l ru.UTF-8
В этом пакете содержится все необходимое для разработки программ,
которые работают с jpeg-изображениями включая документацию.

%description devel -l tr.UTF-8
Bu paket, jpeg resimlerini işleyen programlar geliştirmeniz için
gereken başlık dosyalarını, kitaplıkları ve ilgili yardım belgelerini
içerir.

%description devel -l uk.UTF-8
Цей пакет містить все необхідне для розробки програм, котрі працюють з
jpeg-зображеннями, включаючи документацію.

%package progs
Summary:	Simple clients for manipulating jpeg images
Summary(de.UTF-8):   Einfachen Clients zur Manipulation von jpeg
Summary(fr.UTF-8):   Clients simples pour manipuler de telles images
Summary(pl.UTF-8):   Kilka prostych programów do manipulowania na plikach jpeg
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description progs
Simple clients for manipulating jpeg images. Libjpeg client programs
include cjpeg, djpeg, jpegtran, rdjpgcom and wrjpgcom. Djpeg
decompresses a JPEG file into a regular image file. Jpegtran can
perform various useful transformations on JPEG files. Rdjpgcom
displays any text comments included in a JPEG file. Wrjpgcom inserts
text comments into a JPEG file.

%description progs -l de.UTF-8
Einfachen Clients zur Manipulation von jpeg.

%description progs -l fr.UTF-8
Clients simples pour manipuler de telles images.

%description progs -l pl.UTF-8
Kilka prostych programów do manipulowania na plikach jpeg.

%package static
Summary:	Static libraries for developing programs using libjpeg
Summary(pl.UTF-8):   Biblioteki statyczne libjpeg
Summary(pt_BR.UTF-8):   Bibliotecas estáticas para desenvolvimento com libjpeg
Summary(ru.UTF-8):   Статическая библиотека для программирования с libjpeg
Summary(uk.UTF-8):   Статична бібліотека для програмування з libjpeg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for developing programs using libjpeg.

%description static -l pl.UTF-8
Statyczna biblioteka libjpeg.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com libjpeg.

%description static -l ru.UTF-8
Этот пакет содержит статические библиотеки, необходимые для написания
программ, использующих libjpeg.

%description static -l uk.UTF-8
Цей пакет містить статичні бібліотеки, необхідні для написання
програм, що використовують libjpeg.

%prep
%setup  -q -n jpeg-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%if %{with crop}
gzip -dc %{SOURCE2} | tar xf -
%endif

cp -f %{_datadir}/libtool/config.sub .

%build
%configure \
	--enable-shared \
	--enable-static

%{__make} \
	libdir=%{_libdir}

LD_PRELOAD=$PWD/.libs/%{name}.so make test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_bindir},%{_mandir}/man1}


%{__make} install install-headers install-lib \
	libdir=%{_libdir} \
	DESTDIR=$RPM_BUILD_ROOT

install jversion.h $RPM_BUILD_ROOT%{_includedir}

# remove HAVE_STD{DEF,LIB}_H
# (not necessary but may generate warnings confusing autoconf)
(cd $RPM_BUILD_ROOT%{_includedir}
grep -v 'HAVE_STD..._H' jconfig.h > jconfig.h.new
mv -f jconfig.h.new jconfig.h
)

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {libjpeg,structure}.doc

%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
