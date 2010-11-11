Name:		pam_mount
Version:	2.6
Release:	%mkrel 1
Summary:	Pluggable Authentication Module for dynamic mounting of remote volumes
Summary(pt_BR):	Módulo de autenticação PAM para montagem dinâmica de volumes remotes
Summary(es):	MÃ³dulo de autenticaciÃ³n PAM para montar de forma dinÃ¡mica mvolÃºmenes remotos
License:	GPLv2+ and LGPLv2+
Group:		Networking/Other
URL:		http://pam-mount.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/pam-mount/%{name}-%{version}.tar.xz
Source1:	http://prdownloads.sourceforge.net/pam-mount/%{name}-%{version}.tar.xz.asc
Requires:	opensc
BuildRequires:	pam-devel
BuildRequires:	zlib-devel
BuildRequires:	glib2-devel
BuildRequires:	libHX-devel >= 2.7
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel
BuildRequires:	cryptsetup-devel >= 1.1.2
Obsoletes:	pam_mount-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

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

%prep
%setup -q

%build
%configure2_5x
%make moduledir=/%{_lib}/security

%install
rm -rf %{buildroot}
%makeinstall_std moduledir=/%{_lib}/security
install -m0600 config/pam_mount.conf.xml -D %{buildroot}%{_sysconfdir}/security/pam_mount.conf.xml

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc doc/bugs.txt doc/changelog.txt doc/faq.txt doc/todo.txt doc/pam_mount.txt
/%{_lib}/security/pam_mount*.so
%{_sbindir}/pmt-ehd
%{_sbindir}/pmvarrun
/sbin/mount.crypt
/sbin/mount.crypto_LUKS
/sbin/mount.crypt_LUKS
/sbin/mount.encfs13
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
