Summary:	DNSSEC Zone Key Tool
Name:		zkt
Version:	0.97
Release:	%mkrel 1
License:	BSD-like
Group:		Networking/Other
URL:		http://sourceforge.net/projects/zkt
Source0:	http://kent.dl.sourceforge.net/sourceforge/zkt/%{name}-%{version}.tar.gz
BuildRequires:	bind
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
DNSSEC Zone Key Tool is a toolkit written in C for DNSSEC zone and key
management. It supports automatic zone resigning and KSK- and ZSK rollover
according to RFC4641 and RFC5011. 

%prep

%setup -q -n %{name}-%{version}

%build
export PATH="$PATH:%{_sbindir}"

%configure2_5x \
    --enable-configpath=/var/lib/named

perl -pi -e "s|^#define BIND_VERSION .*|#define BIND_VERSION 940|g" config.h

make OPTIM="%{optflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man8

install -m0755 dnssec-signer %{buildroot}%{_bindir}/
install -m0755 dnssec-zkt %{buildroot}%{_bindir}/
install -m0755 zkt-soaserial %{buildroot}%{_bindir}/

install -m0644 dnssec-signer.8 %{buildroot}%{_mandir}/man8/
install -m0644 dnssec-zkt.8 %{buildroot}%{_mandir}/man8/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG LICENSE README README.logging TODO
%{_bindir}/*
%{_mandir}/man8/*

