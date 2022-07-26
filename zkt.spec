%global optflags %{optflags} -fcommon

Summary:	DNSSEC Zone Key Tool
Name:		zkt
Version:	1.1.4
Release:	1
License:	BSD-like
Group:		Networking/Other
URL:		http://sourceforge.net/projects/zkt
Source0:    https://www.hznet.de/dns/zkt/zkt-%{version}.tar.gz
# Old source
#Source0:	http://kent.dl.sourceforge.net/sourceforge/zkt/%{name}-%{version}.tar.gz
BuildRequires:	bind

%description
DNSSEC Zone Key Tool is a toolkit written in C for DNSSEC zone and key
management. It supports automatic zone resigning and KSK- and ZSK rollover
according to RFC4641 and RFC5011. 

%prep
%setup -q -n %{name}-%{version}

%build
#export PATH="$PATH:%{_sbindir}"

%configure \
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


%files
%defattr(-,root,root)
%doc CHANGELOG LICENSE README README.logging TODO
%{_bindir}/*
%{_mandir}/man8/*



%changelog
* Mon Sep 21 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.97-2mdv2010.0
+ Revision: 446347
- rebuild

* Fri Oct 10 2008 Oden Eriksson <oeriksson@mandriva.com> 0.97-1mdv2009.1
+ Revision: 291412
- fix build
- import zkt


* Fri Oct 10 2008 Oden Eriksson <oeriksson@mandriva.com> 0.97-1mdv2009.0
- initial Mandriva package
