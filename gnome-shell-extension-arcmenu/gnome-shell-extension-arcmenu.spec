%global extdir      arcmenu@arcmenu.com
%global gschemadir  %{_datadir}/glib-2.0/schemas

Name:           gnome-shell-extension-arcmenu
Version:        58
Release:        %autorelease
Summary:        Application Menu Extension for GNOME

License:        GPLv2
URL:            https://gitlab.com/arcmenu/ArcMenu
Source0:        https://gitlab.com/arcmenu/ArcMenu/-/archive/v%{version}/ArcMenu-v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  %{_bindir}/glib-compile-schemas
Requires:       gnome-shell-extension-common

%description
ArcMenu is an application menu for GNOME Shell, designed to provide a more
familiar user experience and workflow. This extension has many features,
including various menu layout styles, GNOME search, quick access to system
shortcuts, and much more!


%prep
%autosetup -n ArcMenu-v%{version}


%build
make mergepo
make extension


%install
mkdir -p %{buildroot}%{gschemadir}
make DESTDIR=%{buildroot} install
cp -pr schemas/org.gnome.shell.extensions.arcmenu.gschema.xml %{buildroot}%{gschemadir}
%find_lang arcmenu

# Fedora and EPEL 8 handles post scripts via triggers
%if 0%{?rhel} && 0%{?rhel} <= 7
%postun
if [ $1 -eq 0 ]; then
  %{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || true
fi

%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || true
%endif


%files -f arcmenu.lang
%license COPYING
%{_datadir}/gnome-shell/extensions/%{extdir}
%{gschemadir}


%changelog
%autochangelog
