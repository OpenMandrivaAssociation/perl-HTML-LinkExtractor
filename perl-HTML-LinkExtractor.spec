%define name perl-HTML-LinkExtractor
%define real_name HTML-LinkExtractor
%define version 0.13
%define release %mkrel 2

Summary: 	Perl extension for extracting links from HTML

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
Source: 	http://search.cpan.org/CPAN/authors/id/R/RA/RADOS/%{real_name}-%{version}.tar.bz2
Url: 		http://search.cpan.org/dist/%{real_name}/
BuildRequires:	perl-devel
BuildRequires:	perl-HTML-TokeParser-Simple
BuildRequires:	perl-URI
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-buildroot/
Requires: 	perl

%description
Perl extension for extracting links from HTML. It is very similar
to HTML::LinkExtor|HTML::LinkExtor, except that besides getting
the URL, you also get the link-text.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix}
make OPTIMIZE="$RPM_OPT_FLAGS" PREFIX=%{_prefix}
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/HTML/LinkExtractor.pm
%{_mandir}/*/*


