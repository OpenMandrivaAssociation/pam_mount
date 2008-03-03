Name:		pam_mount
Version:	0.33
Release:	%mkrel 1
Summary:	Pluggable Authentication Module for dynamic mounting of remote volumes
Summary(pt_BR):	Módulo de autenticação PAM para montagem dinâmica de volumes remotes
Summary(es):	Pluggable authentication module for dynamic mouting of remote volumes
License:	GPLv2+ and LGPLv2+
Group:		Networking/Other
URL:		http://pam-mount.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/pam-mount/%{name}-%{version}.tar.bz2
# patch to use pkcs15-crypt to decrypt a filesystem key file
# based on http://keitin.net/jarpatus/projects/usbtoken/index_eng.shtml
Patch:		pam_mount-0.32-scsupport.patch
Requires:	opensc
BuildRequires:	pam-devel
BuildRequires:	zlib-devel
BuildRequires:	glib2-devel
BuildRequires:	libHX-devel
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%patch -p1 -b .sc

%build
%configure2_5x
%make moduledir=/%{_lib}/security

%install
rm -rf %{buildroot}
%makeinstall_std moduledir=/%{_lib}/security
install -m0600 config/pam_mount.conf.xml -D %{buildroot}%{_sysconfdir}/security/pam_mount.conf.xml
install -m0755 scripts/convert_pam_mount_conf.pl %{buildroot}%{_sbindir}

%clean
rm -rf %{buildroot}

%pre
#
# On upgrade, when pmt.conf exists and pmt.conf.xml does not,
# create pmt.conf.xml with size 0 to signal conversion.
#
f="%{_sysconfdir}/security/pam_mount.conf";
if [ "$1" -eq 2 -a -e "$f" ]; then
	touch -a "$f.xml";
fi;

%post
#
# pmt.conf.xml always exists now.
#
f="%{_sysconfdir}/security/pam_mount.conf";
if [ -e "$f" -a ! -s "$f.xml" ]; then
	"%{_sbindir}ls /convert_pam_mount_conf.pl" \
		<"$f" >"$f.xml";
	echo -en "Configuration migration from pam_mount.conf to pam_mount.conf.xml ";
	if [ "$?" -eq 0 ]; then
		echo "successful - also please check any ~/.pam_mount.conf files.";
	else
		echo "failed";
	fi;
fi;

%files 
%defattr(0644,root,root,0755)
/%{_lib}/security/pam_mount*.so
%attr(0755,root,root) %{_bindir}/*
%attr(0755,root,root) %{_sbindir}/*
%attr(0755,root,root) /sbin/*
%config(noreplace) %{_sysconfdir}/security/%{name}.conf.xml
%doc doc/bugs.txt doc/changelog.txt doc/faq.txt doc/todo.txt doc/pam_mount.txt
%{_mandir}/man8/*
%{_mandir}/man1/mkehd.1*

