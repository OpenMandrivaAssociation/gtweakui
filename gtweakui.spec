%define oname gTweakUI
Summary:        Extra configuration dialogues for gnome
Name:           gtweakui
Version: 0.4.0
Release:        9
Group:          Graphical desktop/GNOME
URL:            https://gtweakui.sourceforge.net/
License:        GPL
Source0:        http://prdownloads.sourceforge.net/gtweakui/%{oname}-%{version}.tar.bz2
BuildRequires:  pkgconfig(libgnomeui-2.0) >= 2.4.0
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
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-Configuration-GNOME-Advanced" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

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


%changelog
* Wed Jul 27 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.0-8mdv2012.0
+ Revision: 691853
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0-7mdv2011.0
+ Revision: 246725
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0-5mdv2008.1
+ Revision: 148209
- drop old menu
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Aug 03 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.0-5mdv2008.0
+ Revision: 58478
- Import gtweakui



* Wed Aug  2 2006 Götz Waschk <waschk@mandriva.org> 0.4.0-5mdv2007.0
- xdg menu

* Fri Sep 02 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.0-4mdk
- rebuild to remove glitz dep

* Wed Aug 24 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.0-3mdk
- Rebuild

* Fri Aug 13 2004 Götz Waschk <waschk@linux-mandrake.com> 0.4.0-2mdk
- fix buildrequires

* Thu Aug 12 2004 Götz Waschk <waschk@linux-mandrake.com> 0.4.0-1mdk
- add icons to the menu
- enable startup notification
- add gtweakui-galeon
- add locale files
- New release 0.4.0

* Thu Jun 10 2004 Götz Waschk <waschk@linux-mandrake.com> 0.0.6-2mdk
- fix buildrequires

* Wed Jun  9 2004 Götz Waschk <waschk@linux-mandrake.com> 0.0.6-1mdk
- initial mdk package

* Sun May 30 2004 Daniel James <daniel@netbreeze.com.au>
- Fixed the issue with the session splash preview not displaying for gnome 2.6
- Updated build system to check for new gtk file chooser dialog
- Use new gtk file chooser dialog if it is available.

* Fri May 28 2004 Daniel James <daniel@netbreeze.com.au>
- Made session.c more usable - second dialog is much nicer now.

* Thu May 27 2004 Daniel James <daniel@netbreeze.com.au>
- Added notice dialog: tells the use which settings require restart
- Added notices to menus.c
- Finished session.c - second dialog completed.
- Added notices to session.c

* Tue May 25 2004 Daniel James <daniel@netbreeze.com.au>
- Better about dialog.

* Mon Feb 24 2003 Daniel James daniel@netbreeze.com.au 0.0.1
- Initial RPM release.
