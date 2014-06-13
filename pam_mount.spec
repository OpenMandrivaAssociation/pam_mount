%define major 0
%define libname %mklibname cryptmount %{major}
%define devname %mklibname cryptmount -d

Summary:	Pluggable Authentication Module for dynamic mounting of remote volumes
Name:		pam_mount
Version:	2.13
Release:	7
License:	GPLv2+ and LGPLv2+
Group:		Networking/Other
Url:		http://pam-mount.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/pam-mount/%{name}-%{version}.tar.xz
Source1:	http://prdownloads.sourceforge.net/pam-mount/%{name}-%{version}.tar.xz.asc
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libcryptsetup)
BuildRequires:	pkgconfig(libHX) >= 3.12
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(mount)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)
Requires:	opensc
Obsoletes:	pam_mount-devel

%description
Pam_mount is a PAM module that allows dynamic remote volume mounting.
It is mainly useful for users that have private volumes in Samba /
Windows NT / Netware servers and need access to them during a Unix
session.

%package -n %{libname}
Summary:	Library for mounting crypto images and handle key files

%description -n %{libname}
Library for mounting crypto images and handle key files.

%package -n %{devname}
Summary:	Development files for %{libname}
Requires:	%{libname} = %{EVRD}
Provides:	libcryptmount-devel = %{EVRD}

%description -n %{devname}
Development files for %{libname} - library for mounting crypto images
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
%doc doc/bugs.txt doc/changelog.txt doc/faq.txt doc/todo.txt doc/pam_mount.txt
%{_libdir}/security/pam_mount*.so
%{_sbindir}/pmt-ehd
%{_sbindir}/pmvarrun
/sbin/mount.crypt
/sbin/mount.crypto_LUKS
/sbin/mount.crypt_LUKS
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

%files  -n %{libname}
%{_libdir}/libcryptmount.so.%{major}*

%files  -n %{devname}
%{_libdir}/libcryptmount.so
%{_libdir}/pkgconfig/libcryptmount.pc
%{_includedir}/libcryptmount.h

