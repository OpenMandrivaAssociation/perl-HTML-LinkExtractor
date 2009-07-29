%define upstream_name    HTML-LinkExtractor
%define upstream_version 0.13

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary: 	Perl extension for extracting links from HTML
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url: 		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/R/RA/RADOS/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-HTML-TokeParser-Simple
BuildRequires:	perl-URI
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
Perl extension for extracting links from HTML. It is very similar
to HTML::LinkExtor|HTML::LinkExtor, except that besides getting
the URL, you also get the link-text.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
