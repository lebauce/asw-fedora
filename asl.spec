%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Name:           asl
Version:        1.42
Release:        1%{?dist}
Summary:        The Macroassembler AS

License:        GPLv2 
URL:            http://john.ccac.rwth-aachen.de:8000/as
Source0:        http://john.ccac.rwth-aachen.de:8000/ftp/as/source/c_version/asl-current.tar.bz2
Source1:        Makefile.def

BuildRequires:  make

%description
AS is a portable macro cross assembler for a variety of microprocessors
and -controllers. Though it is mainly targeted at embedded processors
and single-board computers, you also find CPU families in the target
list that are used in workstations and PCs. 

%prep
%setup -n asl-current
cp -p %SOURCE1 .
%ifarch x86_64
sed -i s:/lib/:/lib64/: Makefile.def
%endif

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT/usr/share/doc/asl/COPYING

%files
%license COPYING
%doc README README.LANGS
%{_mandir}/man1/*
%{_bindir}/*
%{_libdir}/asl
%{_includedir}/asl/*
%{_defaultdocdir}/asl/*.tex

%changelog
* Mon Aug  8 2016 Sylvain Baubeau <sbaubeau@redhat.com>
- Initial release
