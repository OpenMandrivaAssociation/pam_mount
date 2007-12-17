%define	name	pam_mount
%define	version	0.17
%define	release	%mkrel 1
#arg, still no libtool-1.5
#%define	__libtoolize	/bin/true
#%define __cputoolize /bin/true

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Pluggable Authentication Module for dynamic mounting of remote volumes
Summary(pt_BR):	Módulo de autenticação PAM para montagem dinâmica de volumes remotes
Summary(es):	Pluggable authentication module for dynamic mouting of remote volumes
License:	GPL
Group:		Networking/Other
URL:		http://pam-mount.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# patch to use pkcs15-crypt to decrypt a filesystem key file
# based on http://keitin.net/jarpatus/projects/usbtoken/index_eng.shtml
Patch:		pam_mount-0.10.0-scsupport.patch
# support for reading PIN from stdin was added to this specific
# release (0.10.0-5mdk) and we need it due to the patch above
Requires:	opensc >= 0.10.0-5mdk
BuildRequires:	pam-devel, zlib-devel
BuildRequires:	glib2-devel

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

%package devel
Summary: Development files for pam_mount
Requires: pam_mount
Group: Networking/Other

%description devel
Use pam_mount-devel if you need to, for development purpose.

%prep
%setup -q
%patch -p1 -b .sc

%build
%configure
#JMD: you need this if zlib-devel is installed.. weird!
#This is due to a change in source on March 10 2004
perl -pi -e "s|-lcrypto|-lcrypto -lz|" src/Makefile
%make moduledir=/%{_lib}/security

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/sbin
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}/%{_lib}/security
mkdir -p %{buildroot}/%{_includedir}/pam_mount
%makeinstall_std moduledir=/%{_lib}/security
install -m0600 config/pam_mount.conf -D $RPM_BUILD_ROOT%{_sysconfdir}/security/pam_mount.conf

%clean
rm -rf %{buildroot}

%files 
%defattr(0644,root,root,0755)
/%{_lib}/security/pam_mount*.so
%attr(0755,root,root) %{_bindir}/*
%attr(0755,root,root) %{_sbindir}/*
%attr(0755,root,root) /sbin/*
%config(noreplace) %{_sysconfdir}/security/%{name}.conf
%doc AUTHORS ChangeLog COPYING FAQ INSTALL NEWS README TODO
%{_mandir}/man8/*
%{_mandir}/man1/mkehd.1*

%files devel
%defattr(0644,root,root,0755)
/%{_lib}/security/*a
%{_includedir}/*


