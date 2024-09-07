%global extdir      kimpanel@kde.org
%global gschemadir  %{_datadir}/glib-2.0/schemas

Name:           gnome-shell-extension-kimpanel
Version:        master
Release:        %autorelease
Summary:        KDE kimpanel protocol for gnome shell

License:        GPLv2
URL:            https://github.com/wengxt/gnome-shell-extension-kimpanel
Source0:        https://github.com/wengxt/gnome-shell-extension-kimpanel/archive/master.tar.gz

BuildArch:      noarch

BuildRequires:  gettext cmake
BuildRequires:  %{_bindir}/glib-compile-schemas
Requires:       gnome-shell-extension-common

%description
This extension implements the KDE kimpanel protocol for gnome shell. It
provides a native pop-up window for input method listings and an app-
indicator based tray icon for configurations.


%prep
%autosetup


%build
%cmake
%cmake_build
glib-compile-schemas --strict --targetdir=schemas/ schemas


%install
mkdir -p %{buildroot}%{gschemadir}
%cmake_install
cp -pr schemas/org.gnome.shell.extensions.kimpanel.gschema.xml %{buildroot}%{gschemadir}
%find_lang gnome-shell-extensions-kimpanel


# Fedora and EPEL 8 handles post scripts via triggers
%if 0%{?rhel} && 0%{?rhel} <= 7
%postun
if [ $1 -eq 0 ]; then
  %{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || true
fi

%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || true
%endif


%files -f gnome-shell-extensions-kimpanel.lang
%license COPYING
%{_datadir}/gnome-shell/extensions/%{extdir}/metadata.json
%{_datadir}/gnome-shell/extensions/%{extdir}/stylesheet.css
%{_datadir}/gnome-shell/extensions/%{extdir}/*.js
%{_datadir}/gnome-shell/extensions/%{extdir}/schemas
%{gschemadir}


%changelog
%autochangelog
