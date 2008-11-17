Name:		pam_mount
Version:	1.3
Release:	%mkrel 1
Summary:	Pluggable Authentication Module for dynamic mounting of remote volumes
Summary(pt_BR):	Módulo de autenticação PAM para montagem dinâmica de volumes remotes
Summary(es):	Pluggable authentication module for dynamic mouting of remote volumes
License:	GPLv2+ and LGPLv2+
Group:		Networking/Other
URL:		http://pam-mount.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/pam-mount/%{name}-%{version}.tar.lzma
Requires:	opensc
BuildRequires:	pam-devel
BuildRequires:	zlib-devel
BuildRequires:	glib2-devel
BuildRequires:	libHX-devel >= 1.25
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%defattr(0644,root,root,0755)
/%{_lib}/security/pam_mount*.so
%attr(0755,root,root) %{_bindir}/*
%attr(0755,root,root) %{_sbindir}/*
%attr(0755,root,root) /sbin/*
%config(noreplace) %{_sysconfdir}/security/%{name}.conf.xml
%doc doc/bugs.txt doc/changelog.txt doc/faq.txt doc/todo.txt doc/pam_mount.txt
%{_mandir}/man8/*
%{_mandir}/man1/*
%{_mandir}/man5/pam_mount.conf.5*
