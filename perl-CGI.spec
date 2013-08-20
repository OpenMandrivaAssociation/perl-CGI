%define	modname	CGI
%define	modver	3.63

Summary:	Simple Common Gateway Interface class for Perl
Name:		perl-%{modname}
Epoch:		1
Version:	%{perl_convert_version %{modver}}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://stein.cshl.org/WWW/software/CGI/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MARKSTOS/%{modname}.pm-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(FCGI)
BuildRequires:	perl-devel

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
%setup -qn %{modname}.pm-%{modver}
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

