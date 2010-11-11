%define upstream_name	 CGI
%define upstream_version 3.50

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Epoch:      1

Summary:    Simple Common Gateway Interface class for Perl
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://stein.cshl.org/WWW/software/CGI/
Source0:    http://search.cpan.org/CPAN/authors/id/L/LD/LDS/%{upstream_name}.pm-%{upstream_version}.tar.gz

BuildRequires:  perl(FCGI)

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

Requires:       perl >= 0:5.004
Conflicts:      perl < 0:5.600-28mdk

%description
This perl library uses perl5 objects to make it easy to create
Web fill-out forms and parse their contents.  This package
defines CGI objects, entities that contain the values of the
current query string and other state variables.  Using a CGI
object's methods, you can examine keywords and parameters
passed to your script, and create forms whose initial values
are taken from the current query (thereby preserving state
information).

%package Fast
Group:		Development/Perl
Summary: 	CGI Interface for Fast CGI
Requires:	%{name} = %{epoch}:%{version}

%description Fast
CGI::Fast is a subclass of the CGI object created by CGI.pm. It is
specialized to work well with the Open Market FastCGI standard, which
greatly speeds up CGI scripts by turning them into persistently running
server processes.  Scripts that perform time-consuming initialization
processes, such as loading large modules or opening persistent database
connections, will see large performance improvements.

%prep
%setup -q -n %{upstream_name}.pm-%{upstream_version}
perl -pi -e s,/usr/local/bin/perl,/usr/bin/perl, examples/*.{cgi,pl}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%{__rm} -rf %{buildroot}

%makeinstall_std

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README *.html examples
%{perl_vendorlib}/CGI
%exclude %{perl_vendorlib}/CGI/Fast.pm
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*
%exclude %{_mandir}/man3/CGI::Fast.3pm.*

%files Fast
%defattr(-,root,root)
%{perl_vendorlib}/CGI/Fast.pm
%{_mandir}/man3/CGI::Fast.3pm.*
