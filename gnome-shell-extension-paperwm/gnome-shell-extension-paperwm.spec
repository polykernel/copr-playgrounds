%global extdir      paperwm@paperwm.github.com
%global gschemadir  %{_datadir}/glib-2.0/schemas

Name:           gnome-shell-extension-paperwm
Version:        46.17.0
Release:        %autorelease
Summary:        Tiled scroll-able window management for Gnome Shell

License:        GPLv3
URL:            https://github.com/paperwm/PaperWM
Source0:        https://github.com/paperwm/PaperWM/archive/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  %{_bindir}/glib-compile-schemas
Requires:       gnome-shell-extension-common

%description
PaperWM is a Gnome Shell extension which provides scroll-able tiling of windows
and per monitor workspaces. It's inspired by paper notebooks and tiling window
managers.


%prep
%autosetup -n PaperWM-%{version}


%build
glib-compile-schemas --strict --targetdir=schemas/ schemas


%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{extdir}
mkdir -p %{buildroot}%{gschemadir}
cp -pr schemas/org.gnome.shell.extensions.paperwm.gschema.xml %{buildroot}%{gschemadir}
cp -pr --parents metadata.json stylesheet.css *.js \
  config/user.js config/user.css *.ui \
  schemas/gschemas.compiled schemas/org.gnome.shell.extensions.paperwm.gschema.xml \
  resources/ \
  %{buildroot}%{_datadir}/gnome-shell/extensions/%{extdir}


# Fedora and EPEL 8 handles post scripts via triggers
%if 0%{?rhel} && 0%{?rhel} <= 7
%postun
if [ $1 -eq 0 ]; then
  %{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || true
fi

%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || true
%endif


%files
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{extdir}
%{gschemadir}


%changelog
%autochangelog
