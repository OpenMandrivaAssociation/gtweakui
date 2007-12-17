%define oname gTweakUI
Summary:        Extra configuration dialogues for gnome
Name:           gtweakui
Version: 0.4.0
Release:        %mkrel 5
Group:          Graphical desktop/GNOME
URL:            http://gtweakui.sourceforge.net/
License:        GPL
Source0:        http://prdownloads.sourceforge.net/gtweakui/%{oname}-%{version}.tar.bz2
BuildRequires:  libgnomeui2-devel >= 2.4.0
BuildRequires:  libglade2.0-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  desktop-file-utils

%description
With gTweakUI you can configure the GNOME desktop using extra
configuration dialogs.

%prep
%setup -q -n %oname-%version

%build
%configure2_5x
%make
  
%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang gTweakUI
install -d -m 755 $RPM_BUILD_ROOT%{_menudir}
cat >$RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}): \
	command="%{_bindir}/gtweakui-menus" \
	needs="gnome" \
	section="System/Configuration/GNOME/Advanced" \
	title="Menus" \
	startup_notify="true" \
	icon="%_datadir/gTweakUI/g.png" \
	longtitle="Extra preferences for application menus" xdg="true"
?package(%{name}): \
	command="%{_bindir}/gtweakui-session" \
	needs="gnome" \
	section="System/Configuration/GNOME/Advanced" \
	title="Session" \
	startup_notify="true" \
	icon="%_datadir/gTweakUI/g.png" \
	longtitle="Extra session preferences" xdg="true"
?package(%{name}): \
	command="%{_bindir}/gtweakui-nautilus" \
	needs="gnome" \
	section="System/Configuration/GNOME/Advanced" \
	title="Nautilus" \
	startup_notify="true" \
	icon="%_datadir/gTweakUI/g.png" \
	longtitle="Extra nautilus preferences" xdg="true"
?package(%{name}): \
	command="%{_bindir}/gtweakui-galeon" \
	needs="gnome" \
	section="System/Configuration/GNOME/Advanced" \
	title="Galeon" \
	startup_notify="true" \
	icon="%_datadir/gTweakUI/g.png" \
	longtitle="Extra galeon preferences" xdg="true"
EOF
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-Configuration-GNOME-Advanced" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%clean
rm -rf %{buildroot}

%post
%update_menus

%postun
%clean_menus

%files -f gTweakUI.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog NEWS README TODO FAQ
%{_bindir}/gtweakui-galeon
%{_bindir}/gtweakui-menus
%{_bindir}/gtweakui-session
%{_bindir}/gtweakui-nautilus
%_datadir/%oname
%{_datadir}/applications/gtweakui-galeon.desktop
%{_datadir}/applications/gtweakui-menus.desktop
%{_datadir}/applications/gtweakui-session.desktop
%{_datadir}/applications/gtweakui-nautilus.desktop
%_menudir/%name
