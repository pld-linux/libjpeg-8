#
# Conditional build:
%bcond_with	arith	# arithmetic coding support (changes error codes in ABI, patent problems somewhere)
%bcond_with	crop	# lossless cropping support (changes error codes in ABI)
#
Summary:	Library for handling different JPEG files
Summary(de.UTF-8):	Library zum Verarbeiten verschiedener JPEG-Dateien
Summary(es.UTF-8):	Biblioteca para manipulación de diferentes archivos JPEGs
Summary(fr.UTF-8):	Bibliothèque pour gérer différents fichiers JPEG
Summary(pl.UTF-8):	Biblioteka do manipulacji plikami w formacie JPEG
Summary(pt_BR.UTF-8):	Biblioteca para manipulação de diferentes arquivos JPEGs
Summary(ru.UTF-8):	Библиотека для обработки различных JPEG-файлов
Summary(tr.UTF-8):	JPEG resimlerini işleme kitaplığı
Summary(uk.UTF-8):	Бібліотека для обробки різноманітних JPEG-файлів
Name:		libjpeg
Version:	6b
Release:	28
License:	distributable
Group:		Libraries
Source0:	ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v%{version}.tar.gz
# Source0-md5:	dbd5f3b47ed13132f04c685d608a7547
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	d6342c015a489de275ada637a77dc2b0
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-arm.patch
Patch2:		%{name}-include.patch
Patch3:		%{name}-c++.patch
Patch4:		%{name}-libtool.patch
# from http://sylvana.net/jpeg-ari/jpeg-ari-28mar98.tar.gz
Patch5:		%{name}-arith.patch
# from http://sylvana.net/jpegcrop/croppatch.tar.gz
Patch6:		%{name}-crop.patch
URL:		http://www.ijg.org/
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libjpeg package contains a library of functions for manipulating
JPEG images.

%description -l de.UTF-8
Dieses Paket ist eine Library mit Funktionen zur Manipulation von
JPEG-Bildern.

%description -l es.UTF-8
Este paquete contiene una biblioteca de funciones que manipulan
imágenes JPEG.

%description -l fr.UTF-8
Bibliothèque de fonctions qui manipulent des images JPEG.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę funkcji do manipulacji plikami JPEG.

%description -l pt_BR.UTF-8
Este pacote contém uma biblioteca de funções que manipulam imagens
JPEG.

%description -l ru.UTF-8
Библиотека функций для обработки JPEG-изображений и простые клиенты
для такой обработки.

%description -l tr.UTF-8
Bu paket, JPEG şekillerini işlemek için kitaplıklar ve basit
istemciler içerir.

%description -l uk.UTF-8
Бібліотека функцій для обробки JPEG-зображень та прості клієнти для
такої обробки.

%package devel
Summary:	Headers for developing programs using libjpeg
Summary(de.UTF-8):	Header zum Entwickeln von Programmen mit libjpeg
Summary(es.UTF-8):	Archivos de inclusión para desarrollar programas usando libjpeg
Summary(pl.UTF-8):	Pliki nagłówkowe libjpeg
Summary(pt_BR.UTF-8):	Arquivos de inclusão para desenvolver programas usando libjpeg
Summary(ru.UTF-8):	Хедеры для разработки программ, использующих libjpeg
Summary(tr.UTF-8):	libjpeg için geliştirme kitaplıkları ve başlık dosyaları
Summary(uk.UTF-8):	Хедери для розробки програм, що використовують libjpeg
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The libjpeg-devel package includes the header files necessary for
developing programs which will manipulate JPEG files using the libjpeg
library.

%description devel -l de.UTF-8
Dieses Paket bietet alles, was Sie brauchen, um Programme zur
Manipulation von JPEG-Grafiken, einschließlich Dokumentation, zu
entwickeln.

%description devel -l es.UTF-8
Este paquete es todo lo que necesitas para desarrollar programas que
manipulen imágenes JPEG, incluso documentación.

%description devel -l fr.UTF-8
Ce package est tout ce dont vous avez besoin pour développer des
programmes manipulant des images JPEG, et comprend la documentation.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki potrzebne do programowania z wykorzystaniem
biblioteki libjpeg. Zawiera także dokumentację.

%description devel -l pt_BR.UTF-8
Este pacote é tudo que você precisa para desenvolver programas que
manipulam imagens JPEG, incluindo documentação.

%description devel -l ru.UTF-8
В этом пакете содержится все необходимое для разработки программ,
которые работают с JPEG-изображениями включая документацию.

%description devel -l tr.UTF-8
Bu paket, JPEG resimlerini işleyen programlar geliştirmeniz için
gereken başlık dosyalarını, kitaplıkları ve ilgili yardım belgelerini
içerir.

%description devel -l uk.UTF-8
Цей пакет містить все необхідне для розробки програм, котрі працюють з
JPEG-зображеннями, включаючи документацію.

%package static
Summary:	Static library for developing programs using libjpeg
Summary(pl.UTF-8):	Biblioteka statyczna libjpeg
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com libjpeg
Summary(ru.UTF-8):	Статическая библиотека для программирования с libjpeg
Summary(uk.UTF-8):	Статична бібліотека для програмування з libjpeg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static library for developing programs using libjpeg.

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

%package progs
Summary:	Simple clients for manipulating JPEG images
Summary(de.UTF-8):	Einfachen Clients zur Manipulation von JPEG
Summary(fr.UTF-8):	Clients simples pour manipuler des images JPEG
Summary(pl.UTF-8):	Kilka prostych programów do manipulowania na plikach JPEG
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description progs
Simple clients for manipulating JPEG images. Libjpeg client programs
include cjpeg, djpeg, jpegtran, rdjpgcom and wrjpgcom. Djpeg
decompresses a JPEG file into a regular image file. Jpegtran can
perform various useful transformations on JPEG files. Rdjpgcom
displays any text comments included in a JPEG file. Wrjpgcom inserts
text comments into a JPEG file.

%description progs -l de.UTF-8
Einfachen Clients zur Manipulation von JPEG.

%description progs -l fr.UTF-8
Clients simples pour manipuler des images JPEG.

%description progs -l pl.UTF-8
Kilka prostych programów do obróbki plików JPEG, w tym: cjpeg, djpeg,
jpegtran, rdjpgcom i wrjpgcom. djpeg dekompresuje plik JPEG do
zwykłego pliku obrazu, jpegtran potrafi wykonywać różne
przekształcenia na plikach JPEG. rdjpgcom wyświetla komentarze
tekstowe dołączone do pliku JPEG, a wrjpgcom wstawia takie komentarze.

%prep
%setup -q -n jpeg-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%{?with_arith:%patch5 -p1}
%{?with_crop:%patch6 -p1}

%build
%configure \
	--enable-shared \
	--enable-static

%{__make} \
	libdir=%{_libdir}

LD_PRELOAD=$PWD/.libs/%{name}.so \
%{__make} test

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

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README change.log %{?with_arith:README.arithmetic}
%attr(755,root,root) %{_libdir}/libjpeg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjpeg.so.62

%files devel
%defattr(644,root,root,755)
%doc {libjpeg,structure}.doc
%attr(755,root,root) %{_libdir}/libjpeg.so
%{_libdir}/libjpeg.la
%{_includedir}/jconfig.h
%{_includedir}/jerror.h
%{_includedir}/jmorecfg.h
%{_includedir}/jpeglib.h
%{_includedir}/jversion.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libjpeg.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cjpeg
%attr(755,root,root) %{_bindir}/djpeg
%attr(755,root,root) %{_bindir}/jpegtran
%attr(755,root,root) %{_bindir}/rdjpgcom
%attr(755,root,root) %{_bindir}/wrjpgcom
%{_mandir}/man1/cjpeg.1*
%{_mandir}/man1/djpeg.1*
%{_mandir}/man1/jpegtran.1*
%{_mandir}/man1/rdjpgcom.1*
%{_mandir}/man1/wrjpgcom.1*
%lang(fi) %{_mandir}/fi/man1/cjpeg.1*
%lang(pl) %{_mandir}/pl/man1/cjpeg.1*
%lang(pl) %{_mandir}/pl/man1/djpeg.1*
