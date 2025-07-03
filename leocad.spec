%global commit0 7287b621fa7de8c328eae7da2de7628aef6ee347
%global date 20250702
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global tag %{version}

Name:       leocad
Version:    23.03%{!?tag:^%{date}git%{shortcommit0}}
Release:    7%{?dist}
Summary:    Visual brick construction tool for kids
License:    GPLV2+
URL:        http://www.leocad.org

%if 0%{?tag:1}
Source0:    https://github.com/leozide/leocad/archive/refs/tags/v%{version}.tar.gz/#/%{name}-%{version}.tar.gz
%else
Source0:    https://github.com/leozide/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%endif

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-linguist
BuildRequires:  zlib-devel

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
%qmake_qt5 \
  LDRAW_LIBRARY_PATH=%{_datadir}/ldraw \
  DISABLE_UPDATE_CHECK=1

%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

# Let RPM pick the docs in the files section
rm -fr %{buildroot}%{_docdir}/%{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%license docs/COPYING.txt
%doc docs/README.md docs/CREDITS.txt
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/hicolor/*/mimetypes/application-vnd.%{name}.*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man1/%{name}.*

%changelog
* Thu Jul 03 2025 Simone Caronni <negativo17@gmail.com> - 23.03^20250702git7287b62-7
- Update to latest snapshot.

* Fri Jun 27 2025 Simone Caronni <negativo17@gmail.com> - 23.03^20250627gited24c15-6
- Update to latest snapshot.

* Thu Mar 13 2025 Simone Caronni <negativo17@gmail.com> - 23.03^20250224git228fb79-5
- Update to latest snapshot, trim changelog.

* Thu Sep 26 2024 Simone Caronni <negativo17@gmail.com> - 23.03^20240924gitda803dc-4
- Update to latest snapshot.
- Use new packaging guidelines format for snapshots.

* Sun Apr 28 2024 Simone Caronni <negativo17@gmail.com> - 23.03-3.20240428git5f028dc
- Update to latest snapshot.

* Tue Mar 05 2024 Simone Caronni <negativo17@gmail.com> - 23.03-2.20240303gitb6de368
- Update to latest snapshot.
