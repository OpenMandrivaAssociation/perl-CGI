%define	modname	CGI
%define	modver	3.63

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	3
Epoch:		1

Summary:	Simple Common Gateway Interface class for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://stein.cshl.org/WWW/software/CGI/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MARKSTOS/%{modname}.pm-%{modver}.tar.gz

BuildRequires:	perl(FCGI)
BuildRequires:	perl-devel

BuildArch:	noarch

%description
This perl library uses perl5 objects to make it easy to create
Web fill-out forms and parse their contents.  This package
defines CGI objects, entities that contain the values of the
current query string and other state variables.  Using a CGI
object's methods, you can examine keywords and parameters
passed to your script, and create forms whose initial values
are taken from the current query (thereby preserving state
information).

%package	Fast
Group:		Development/Perl
Summary:	CGI Interface for Fast CGI
Requires:	%{name} = %{EVRD}

%description Fast
CGI::Fast is a subclass of the CGI object created by CGI.pm. It is
specialized to work well with the Open Market FastCGI standard, which
greatly speeds up CGI scripts by turning them into persistently running
server processes.  Scripts that perform time-consuming initialization
processes, such as loading large modules or opening persistent database
connections, will see large performance improvements.

%prep
%setup -q -n %{modname}.pm-%{modver}
perl -pi -e s,/usr/local/bin/perl,/usr/bin/perl, examples/*.{cgi,pl}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README *.html examples
%{perl_vendorlib}/CGI
%exclude %{perl_vendorlib}/CGI/Fast.pm
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*
%exclude %{_mandir}/man3/CGI::Fast.3pm.*

%files Fast
%{perl_vendorlib}/CGI/Fast.pm
%{_mandir}/man3/CGI::Fast.3pm.*

%changelog
* Sat Dec 29 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.630.0-1
- cleanups
- new version

* Sun Jan 22 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.530.0-4
+ Revision: 764940
- make sure to really rebuild against perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 3.530.0-3
+ Revision: 763519
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 3.530.0-2
+ Revision: 763045
- rebuild

* Tue Apr 26 2011 Sandro Cazzaniga <kharec@mandriva.org> 3.530.0-1
+ Revision: 659268
- update to 3.53

* Sat Mar 05 2011 Sandro Cazzaniga <kharec@mandriva.org> 3.520.0-1
+ Revision: 642187
- new version

* Wed Jan 05 2011 Oden Eriksson <oeriksson@mandriva.com> 3.510.0-1mdv2011.0
+ Revision: 628941
- 3.51

* Thu Nov 11 2010 Jérôme Quelin <jquelin@mandriva.org> 3.500.0-1mdv2011.0
+ Revision: 595939
- update to 3.50

* Thu Jul 22 2010 Funda Wang <fwang@mandriva.org> 3.490.0-2mdv2011.0
+ Revision: 557002
- rebuild

* Mon Feb 08 2010 Jérôme Quelin <jquelin@mandriva.org> 3.490.0-1mdv2010.1
+ Revision: 502086
- update to 3.49

* Sun Sep 27 2009 Jérôme Quelin <jquelin@mandriva.org> 3.480.0-1mdv2010.0
+ Revision: 449994
- update to 3.48

* Fri Sep 11 2009 Jérôme Quelin <jquelin@mandriva.org> 3.470.0-1mdv2010.0
+ Revision: 438460
- adding missing buildrequires:
- update to 3.47

* Sun Aug 16 2009 Jérôme Quelin <jquelin@mandriva.org> 3.450.0-1mdv2010.0
+ Revision: 416947
- update to 3.45

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.43-1mdv2010.0
+ Revision: 370014
- update to new version 3.43

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 3.39-2mdv2009.1
+ Revision: 351686
- rebuild

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.39-1mdv2009.0
+ Revision: 270343
- update to new version 3.39

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 3.33-2mdv2009.0
+ Revision: 223572
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 3.33-1mdv2008.1
+ Revision: 180554
- 3.33

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri May 18 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 3.29-1mdv2008.0
+ Revision: 28362
- Updated to 3.29.


* Wed Oct 11 2006 Oden Eriksson <oeriksson@mandriva.com>
+ 2006-10-10 09:28:41 (63275)
- use the check macro

* Sat Oct 07 2006 Oden Eriksson <oeriksson@mandriva.com>
+ 2006-10-06 07:09:54 (62902)
- Import perl-CGI

* Thu Feb 09 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.16-1mdk
- 3.16

* Tue Jan 31 2006 Oden Eriksson <oeriksson@mandrakesoft.com> 3.15-1mdk
- 3.15

* Tue May 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.08-1mdk
- 3.08

* Thu Apr 22 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.05-1mdk
- 3.05

* Fri Feb 27 2004 Guillaume Rousse <guillomovitch@mandrake.org> 3.00-2mdk
- fixed perl-CGI-Fast dependency problem

