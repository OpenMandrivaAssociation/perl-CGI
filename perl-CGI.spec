%define upstream_name	 CGI

Name:       perl-%{upstream_name}
Version:    4.66
Release:    1

Summary:    Simple Common Gateway Interface class for Perl

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/pod/CGI
Source0:    http://search.cpan.org/CPAN/authors/id/L/LE/LEEJO/%{upstream_name}-%{version}.tar.gz

BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Test::More)
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
%autosetup -p1 -n %{upstream_name}-%{version}
perl -pi -e s,/usr/local/bin/perl,/usr/bin/perl, examples/*.{cgi,pl}
chmod 755 examples

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc Changes META.json META.yml examples
%{perl_vendorlib}/CGI
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/*.pod
%{_mandir}/man3/*
