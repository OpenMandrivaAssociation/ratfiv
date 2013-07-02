Summary:		Fortran preprocessor
Name:			ratfiv
Version:		1.0.5
Release:		8
License:		GPL
Group:			Development/Other
Buildrequires:		gcc-gfortran
Source0:		%name-%version.tar.bz2
patch0:                 ratfiv-1.0.5-fix-gfortran.patch
URL:			http://sauvy.ined.fr/~brouard/%{name}
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
mkdir -p %{buildroot}/%_bindir
install -m755 stage1/ratfiv %{buildroot}/%_bindir
install -m755 ratfor %{buildroot}/%_bindir/ratforf77
mkdir -p %{buildroot}/%_mandir/man1
install -m644 doc/ratfiv.man %{buildroot}/%_mandir/man1/ratfiv.1

%clean

%files
%doc README doc/%{name}.doc doc/%{name}.pdf doc/%{name}.html
%{_bindir}/*
%{_mandir}/man1/*






%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0.5-7mdv2010.0
+ Revision: 433059
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.5-6mdv2009.0
+ Revision: 260046
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.5-5mdv2009.0
+ Revision: 247889
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0.5-3mdv2008.1
+ Revision: 140744
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Mar 22 2007 Lenny Cartier <lenny@mandriva.com> 1.0.5-3mdv2007.1
+ Revision: 148022
- Rename ratfor to ratforf77 to avoid conflict #16482

* Wed Oct 18 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.5-2mdv2007.0
+ Revision: 65850
- Add Patch 0:Allow to build with gfortran
- import ratfiv-1.0.5-2mdk

* Mon Jan 02 2006 Lenny Cartier <lenny@mandriva.com> 1.0.5-2mdk
- rebuild

* Thu Jun 03 2004 Nicolas Brouard <nicolas.brouard@libertysurf.fr> 1.0.5-1mdk 
- initial contribs version of ratfiv package

