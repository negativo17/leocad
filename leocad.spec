%global commit0 3b8b22493a5d7c563185d4a4a956fb8ad1f2e9a7
%global date 20200121
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global tag %{version}

Name:       leocad
Version:    19.07.1
Release:    1%{!?tag:.%{date}git%{shortcommit0}}%{?dist}
Summary:    Visual brick construction tool for kids
License:    GPLV2+
URL:        http://www.leocad.org

%if 0%{?tag:1}
Source0:    https://codeload.github.com/leozide/%{name}/tar.gz/v%{version}#/%{name}-%{version}.tar.gz
%else
Source0:    https://github.com/leozide/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%endif

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  qt5-devel

Requires:       ldraw

%description 
LeoCAD is a CAD program that uses bricks similar to those found in many toys
(but they don't represent any particular brand). Currently it has a library of
more than 1000 different pieces. LEGO is a trademark of the LEGO Group of
companies which does not sponsor, authorize or endorse this software.

%prep
%if 0%{?tag:1}
%autosetup -p1
%else
%autosetup -p1 -n %{name}-%{commit0}
%endif

%build
%qmake_qt5 LDRAW_LIBRARY_PATH=%{_datadir}/ldraw DISABLE_UPDATE_CHECK=1
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

# Let RPM pick the docs in the files section
rm -fr %{buildroot}%{_docdir}/%{name}

%check
appstream-util validate-relax %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%license docs/COPYING.txt
%doc docs/README.txt docs/CREDITS.txt
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/mimetypes/application-vnd.%{name}.svg
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.*

%changelog
* Thu Jan 23 2020 Simone Caronni <negativo17@gmail.com> - 19.07.1-1.20200121git3b8b224
- First build.
