Name: flameshot
Version: 0.8.0
Release: 1%{?dist}
Summary: Powerful yet simple to use screenshot software
Summary(eu-ES): Potente pero simple de usar software de capturas

%global sourcename flameshot

Group: Application
License: GPLv3
URL: https://github.com/flameshot-org/%{sourcename}
Source0: https://github.com/flameshot-org/%{sourcename}/archive/v%{version}.tar.gz

#%%define _binaries_in_noarch_packages_terminate_build   0
#BuildArch: noarch

BuildRequires: gcc-c++  >= 4.9.2  
BuildRequires: pkgconfig(Qt5Core) >= 5.3.0
BuildRequires: pkgconfig(Qt5Gui)  >= 5.3.0
BuildRequires: pkgconfig(Qt5Widgets)  >= 5.3.0
BuildRequires: qt5-qttools-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-qtsvg-devel
BuildRequires: cmake  >= 3.13.0

Requires: qt5-qtbase >= 5.3.0
Requires: qt5-qttools
Requires: qt5-qtsvg

%description
Flameshot is a screenshot software, it's
powerful yet simple to use for GNU/Linux

%prep
%setup -q -n v%{version}

%build
cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%install
%make_install INSTALL_ROOT=%{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/dbus-1/interfaces/org.flameshot.Flameshot.xml
%{_datadir}/dbus-1/services/org.flameshot.Flameshot.service
%{_datadir}/metainfo/flameshot.appdata.xml
%{_datadir}/flameshot/translations
%{_datadir}/applications/%{name}.desktop
%{_datadir}/bash-completions/completions/%{name}
%{_datadir}/icons/hicolor

%changelog
* Mon Sep 07 2020 Zetao Yang <vitzys@outlook.com> - 0.8.0-1
- Updated for flameshot 0.8.0
* Sat Aug 18 2018 Zetao Yang <vitzys@outlook.com> - 0.6.0-1
- Updated for flameshot 0.6.0
- More details, please see https://flameshot.js.org/#/changelog?id=v060
* Tue Jan 09 2018 Zetao Yang <vitzys@outlook.com> - 0.5.0-1
- Initial package for flameshot 0.5.0
- More details, please see https://flameshot.js.org/#/changelog?id=v051

