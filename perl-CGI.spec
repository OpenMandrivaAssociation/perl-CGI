%define upstream_name	 CGI
%define upstream_version 4.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    6
Epoch:      1

Summary:    Simple Common Gateway Interface class for Perl

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://stein.cshl.org/WWW/software/CGI/
Source0:    http://search.cpan.org/CPAN/authors/id/L/LD/LDS/%{upstream_name}.pm-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec) >= 0.820.0
BuildRequires: perl(Test::More) >= 0.980.0
BuildRequires: perl-devel
BuildArch:  noarch

%description
This perl library uses perl5 objects to make it easy to create
Web fill-out forms and parse their contents.  This package
defines CGI objects, entities that contain the values of the
current query string and other state variables.  Using a CGI
object's methods, you can examine keywords and parameters
passed to your script, and create forms whose initial values
are taken from the current query (thereby preserving state
information).

%prep
%setup -q -n %{upstream_name}.pm-%{upstream_version}
perl -pi -e s,/usr/local/bin/perl,/usr/bin/perl, examples/*.{cgi,pl}
chmod 755 examples

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml MYMETA.yml README examples
%{perl_vendorlib}/CGI
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*

