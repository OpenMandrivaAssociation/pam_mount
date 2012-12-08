%define libcryptmount %mklibname cryptmount 0
%define cryptmountdevel %mklibname cryptmount -d
Name:		pam_mount
Version:	2.13
Release:	2
Summary:	Pluggable Authentication Module for dynamic mounting of remote volumes
# Localized summaries should go to specspo
#Summary(pt_BR):	Módulo de autenticação PAM para montagem dinâmica de volumes remotes
#Summary(es):	MÃ³dulo de autenticaciÃ³n PAM para montar de forma dinÃ¡mica mvolÃºmenes remotos
License:	GPLv2+ and LGPLv2+
Group:		Networking/Other
URL:		http://pam-mount.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/pam-mount/%{name}-%{version}.tar.xz
Source1:	http://prdownloads.sourceforge.net/pam-mount/%{name}-%{version}.tar.xz.asc
Requires:	opensc
BuildRequires:	pam-devel
BuildRequires:	zlib-devel
BuildRequires:	glib2-devel
BuildRequires:	pkgconfig(libHX) >= 3.12
BuildRequires:	libxml2-devel >= 2.6
BuildRequires:	libmount-devel >= 2.20
BuildRequires:	openssl-devel
BuildRequires:	cryptsetup-devel >= 1.1.2
Obsoletes:	pam_mount-devel

%description
Pam_mount is a PAM module that allows dynamic remote volume mounting.
It is mainly useful for users that have private volumes in Samba /
Windows NT / Netware servers and need access to them during a Unix
session.

%description -l pt_BR
O pam_mount é um módulo PAM que permite montagem dinâmica de volumes
remotos. Ele é particularmente útil para usuários que detém volumes
privados em servidores Samba / Windows NT / Netware e precisam ter
acesso a eles durante uma sessão Unix.

%description -l fr_FR
pam_mount est un module qui permet de monter dynamiquement un
volume au login. Il est utilisé afin de permettre aux utilisateurs de
monter leur répertoires privés sur des serveurs Samba/NT/Netware au
cours d'une session Unix.

%package -n %libcryptmount
Summary:	Library for mounting crypto images and handle key files
License:	LGPL

%description -n %libcryptmount
Library for mounting crypto images and handle key files.

%package -n %cryptmountdevel
Summary:	Development files for %libcryptmount
License:	LGPL
Requires:	%libcryptmount = %{EVRD}
Provides:	libcryptmount-devel = %{EVRD}

%description -n %cryptmountdevel
Development files for %libcryptmount - library for mounting crypto images
and handle key files.

%prep
%setup -q

%build
%configure2_5x
%make moduledir=%{_libdir}/security

%install
%makeinstall_std moduledir=%{_libdir}/security
install -m0600 config/pam_mount.conf.xml -D %{buildroot}%{_sysconfdir}/security/pam_mount.conf.xml

%files 
%defattr(-,root,root)
%doc doc/bugs.txt doc/changelog.txt doc/faq.txt doc/todo.txt doc/pam_mount.txt
%{_libdir}/security/pam_mount*.so
%{_sbindir}/pmt-ehd
%{_sbindir}/pmvarrun
/sbin/mount.crypt
/sbin/mount.crypto_LUKS
/sbin/mount.crypt_LUKS
#/sbin/mount.encfs13
/sbin/umount.crypt
/sbin/umount.crypt_LUKS
/sbin/umount.crypto_LUKS
%config(noreplace) %{_sysconfdir}/security/%{name}.conf.xml
%{_mandir}/man8/pam_mount.8*
%{_mandir}/man8/pmt-ehd.8*
%{_mandir}/man8/pmvarrun.8*
%{_mandir}/man8/mount.crypt.8*
%{_mandir}/man8/mount.crypt_LUKS.8*
%{_mandir}/man8/mount.crypto_LUKS.8*
%{_mandir}/man8/umount.crypt.8*
%{_mandir}/man8/umount.crypt_LUKS.8*
%{_mandir}/man8/umount.crypto_LUKS.8*
%{_mandir}/man5/pam_mount.conf.5*

%files  -n %libcryptmount
%{_libdir}/libcryptmount.so.*

%files  -n %cryptmountdevel
%{_libdir}/libcryptmount.so
%{_libdir}/pkgconfig/libcryptmount.pc
%{_includedir}/libcryptmount.h


%changelog
* Fri Dec 16 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.13-1mdv2012.0
+ Revision: 743164
- mistype fixed
- add separate packages for libcryptomount
- file list fixed
- update to 2.13

* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.10-1
+ Revision: 674642
- update to new version 2.10

* Sat Apr 09 2011 Funda Wang <fwang@mandriva.org> 2.9-1
+ Revision: 652083
- new verison 2.9

* Sat Jan 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.8-1mdv2011.0
+ Revision: 627302
- update to new version 2.8

* Thu Dec 02 2010 Funda Wang <fwang@mandriva.org> 2.7-1mdv2011.0
+ Revision: 604654
- update to new version 2.7

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.6-1mdv2011.0
+ Revision: 596069
- new version
- hardcode explicit files list

* Sat Aug 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.5-1mdv2011.0
+ Revision: 569592
- update to new version 2.5

* Wed Aug 04 2010 Funda Wang <fwang@mandriva.org> 2.4-3mdv2011.0
+ Revision: 565782
- rebuild for new libHX

* Thu Jul 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.4-2mdv2011.0
+ Revision: 562879
- bump build dependency on cryptsetup-devel

* Wed Jul 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.4-1mdv2011.0
+ Revision: 562713
- update to new version 2.4

* Mon May 03 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.1-1mdv2010.1
+ Revision: 541697
- New 2.1
  New S1
  Fix a little spanish translation

* Mon Apr 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.0-1mdv2010.1
+ Revision: 538861
- new version

* Tue Apr 13 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.36-1mdv2010.1
+ Revision: 534185
- update to new version 1.36

* Sat Apr 10 2010 Funda Wang <fwang@mandriva.org> 1.34-1mdv2010.1
+ Revision: 533546
- new version 1.34

* Wed Apr 07 2010 Funda Wang <fwang@mandriva.org> 1.33-3mdv2010.1
+ Revision: 532509
- rebuild

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 1.33-2mdv2010.1
+ Revision: 511609
- rebuilt against openssl-0.9.8m

* Mon Jan 11 2010 Frederik Himpe <fhimpe@mandriva.org> 1.33-1mdv2010.1
+ Revision: 489868
- update to new version 1.33

* Tue Sep 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.32-1mdv2010.0
+ Revision: 447393
- update to new version 1.32

* Wed Sep 02 2009 Frederik Himpe <fhimpe@mandriva.org> 1.31-1mdv2010.0
+ Revision: 425459
- update to new version 1.31

* Sat Aug 29 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.30-1mdv2010.0
+ Revision: 422176
- update to new version 1.30

* Thu Jul 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.27-1mdv2010.0
+ Revision: 394002
- update to new version 1.27

* Fri Jun 19 2009 Funda Wang <fwang@mandriva.org> 1.26-1mdv2010.0
+ Revision: 387381
- fix BR
- bump BR
- New version 1.26

* Sun May 10 2009 Frederik Himpe <fhimpe@mandriva.org> 1.25-1mdv2010.0
+ Revision: 374032
- update to new version 1.25

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.22-1mdv2010.0
+ Revision: 371938
- update to new version 1.22

* Wed Mar 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.21-1mdv2009.1
+ Revision: 357156
- update to new version 1.21

* Tue Mar 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdv2009.1
+ Revision: 347909
- update to new version 1.20

* Sun Mar 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.19-1mdv2009.1
+ Revision: 346283
- update to new version 1.19

* Mon Feb 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.18-1mdv2009.1
+ Revision: 338707
- update to new version 1.18

* Wed Feb 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.17-1mdv2009.1
+ Revision: 337613
- update to new version 1.17

* Sat Jan 24 2009 Funda Wang <fwang@mandriva.org> 1.16-1mdv2009.1
+ Revision: 333173
- update to new version 1.16

* Wed Jan 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.9-1mdv2009.1
+ Revision: 329386
- update to new version 1.9

* Wed Jan 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.8-1mdv2009.1
+ Revision: 326519
- update to new version 1.8

* Fri Jan 02 2009 Frederik Himpe <fhimpe@mandriva.org> 1.7-1mdv2009.1
+ Revision: 323484
- Update to new version 1.7

* Sat Dec 27 2008 Frederik Himpe <fhimpe@mandriva.org> 1.6-1mdv2009.1
+ Revision: 319895
- Update to new version 1.6

* Sun Dec 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.5-1mdv2009.1
+ Revision: 314306
- new version
- little spec cleanup

* Mon Nov 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.3-1mdv2009.1
+ Revision: 304039
- update to new version 1.3

* Sun Nov 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.2-1mdv2009.1
+ Revision: 303815
- update to new version 1.2

* Thu Oct 23 2008 Frederik Himpe <fhimpe@mandriva.org> 1.1-1mdv2009.1
+ Revision: 296798
- Update to new version 1.1
- Remove lsof patch: not needed anymore
- Remove SmartCard support patch: the code has changed too much
  to be able to integrate this, and it is not supported upstream
- Remove postinstall script which migrates an old configuration file:
  upstream removed the migration script

* Sun Oct 12 2008 Funda Wang <fwang@mandriva.org> 0.49-1mdv2009.1
+ Revision: 292671
- New version 0.49

* Sun Sep 14 2008 Funda Wang <fwang@mandriva.org> 0.48-1mdv2009.0
+ Revision: 284621
- New version 0.48
- rediff patch0
- sync fedora patch with lsof

* Sun Sep 07 2008 Funda Wang <fwang@mandriva.org> 0.47-2mdv2009.0
+ Revision: 282298
- add git patch to build against 1.25

* Fri Sep 05 2008 Frederik Himpe <fhimpe@mandriva.org> 0.47-1mdv2009.0
+ Revision: 281646
- update to new version 0.47

* Mon Sep 01 2008 Frederik Himpe <fhimpe@mandriva.org> 0.45-1mdv2009.0
+ Revision: 278530
- update to new version 0.45

* Thu Jul 17 2008 Funda Wang <fwang@mandriva.org> 0.43-1mdv2009.0
+ Revision: 236672
- New version 0.43

* Sat Jun 21 2008 Buchan Milne <bgmilne@mandriva.org> 0.41-1mdv2009.0
+ Revision: 227831
- New version 0.41

* Sun May 18 2008 Funda Wang <fwang@mandriva.org> 0.37-1mdv2009.0
+ Revision: 208618
- fix file list
- bumpig versioned BR
- New version 0.37

* Sun Mar 23 2008 Emmanuel Andry <eandry@mandriva.org> 0.33-2mdv2008.1
+ Revision: 189605
- Obsoletes pam_mount-devel

* Mon Mar 03 2008 Buchan Milne <bgmilne@mandriva.org> 0.33-1mdv2008.1
+ Revision: 178075
- New version 0.33
-Fix Source URL

* Fri Feb 15 2008 Adam Williamson <awilliamson@mandriva.org> 0.32-2mdv2008.1
+ Revision: 168727
- buildrequires openssl-devel (so it can use openssl algorithms)

* Wed Feb 13 2008 Adam Williamson <awilliamson@mandriva.org> 0.32-1mdv2008.1
+ Revision: 167132
- buildrequires libxml2-devel
- rebuild for new era
- new license policy (scripts are GPLv2+, library is LGPLv2+)
- drop -devel package (not necessary, stuff was removed upstream)
- minor cleanups
- add conversion for config file in %%post and %%pre (from upstream .spec file)
- adjust file list for upstream changes
- rediff patch (hope I got it right)
- new release 0.32 (should fix #37681)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Aug 28 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-08-28 16:06:25 (58356)
- updated to version 0.17
- removed realpath patch, no longer needed
- bunzipped patches

* Mon Aug 28 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-08-28 15:42:07 (58343)
- Import pam_mount

* Fri Jan 20 2006 Buchan Milne <bgmilne@mandriva.org> 0.10.0-5mdk
- glib2-devel instead of glib-devel

* Thu Jan 12 2006 Buchan Milne <bgmilne@mandriva.org> 0.10.0-4mdk
- buildrequire glib-devel

* Mon Dec 05 2005 Andreas Hasenack <andreas@mandriva.com> 0.10.0-3mdk
- added patch to make it possible to use a smart card to decrypt the
  filesystem key file for dm-crypt mounts (based on work done by
  Jari Eskelinen, see 
  http://keitin.net/jarpatus/projects/usbtoken/index_eng.shtml)
- added requirement for a specific opensc EVR due to the above patch
- added symlinks in /sbin for the u?mount.crypt scripts

* Mon Dec 05 2005 Andreas Hasenack <andreas@mandriva.com> 0.10.0-2mdk
- added patch to fix umount.crypt script

* Mon Dec 05 2005 Andreas Hasenack <andreas@mandriva.com> 0.10.0-1mdk
- updated to version 0.10.0
- removed the libtoolize and cputoolize defines, seems to work without them

* Wed Aug 10 2005 Buchan Milne <bgmilne@linux-mandrake.com> 0.9.25-1mdk
- New release 0.9.25

* Tue Nov 16 2004 Jean-Michel Dault <jmdault@mandrakesoft.com> 0.9.20-2mdk
- add FAQ and other missing docs
- buildrequires zlib-devel (See Changelog entry, 10 March 2004)

* Wed Sep 01 2004 Buchan Milne <bgmilne@linux-mandrake.com> 0.9.20-1mdk
- 0.9.20

* Sun Jan 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.9-1mdk
- 0.9.9
- rm -rf $RPM_BUILD_ROOT
- cleanups and cosmetics

