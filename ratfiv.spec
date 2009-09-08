Summary:		Ratfiv fortran preprocessor
Name:			ratfiv
Version:		1.0.5
Release:		%mkrel 7
License:		GPL
Group:			Development/Other
Buildrequires:		gcc-gfortran
Source0:		%name-%version.tar.bz2
patch0:                 ratfiv-1.0.5-fix-gfortran.patch
URL:			http://sauvy.ined.fr/~brouard/%{name}
BuildRoot:		%{_tmppath}/%{name}-buildroot
ExclusiveArch:		%{ix86} ia64 x86_64 amd64

%description
This is ratfiv (ratfor -> rat4 -> rat5) a fortran preprocessor which 
was used on VAX system.

%prep 
%setup -q
%patch0 -p0 

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/%_bindir
install -m755 stage1/ratfiv $RPM_BUILD_ROOT/%_bindir
install -m755 ratfor $RPM_BUILD_ROOT/%_bindir/ratforf77
mkdir -p $RPM_BUILD_ROOT/%_mandir/man1
install -m644 doc/ratfiv.man $RPM_BUILD_ROOT/%_mandir/man1/ratfiv.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README doc/%{name}.doc doc/%{name}.pdf doc/%{name}.html
%{_bindir}/*
%{_mandir}/man1/*




