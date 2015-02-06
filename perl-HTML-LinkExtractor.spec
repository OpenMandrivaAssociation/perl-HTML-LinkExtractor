%define upstream_name    HTML-LinkExtractor
%define upstream_version 0.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl extension for extracting links from HTML
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/R/RA/RADOS/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::TokeParser::Simple)
BuildRequires:	perl(URI)
BuildArch:	noarch

%description
Perl extension for extracting links from HTML. It is very similar
to HTML::LinkExtor|HTML::LinkExtor, except that besides getting
the URL, you also get the link-text.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix}
make OPTIMIZE="%{optflags}" PREFIX=%{_prefix}
make test

%install
%makeinstall PREFIX=%{buildroot}%{_prefix}

%files
%doc Changes README
%{perl_vendorlib}/HTML/LinkExtractor.pm
%{_mandir}/*/*

%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.0
+ Revision: 403255
- rebuild using %%perl_convert_version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.13-2mdv2008.1
+ Revision: 135846
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Jan 03 2007 Stefan van der Eijk <stefan@mandriva.org> 0.13-2mdv2007.0
+ Revision: 103806
- Import perl-HTML-LinkExtractor

* Sun Feb 05 2006 Stefan van der Eijk <stefan@eijk.nu> 0.13-2mdk
- Rebuild
- %%{1}mdv2007.1

* Tue Jan 11 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.13-1mdk
- 0.13
- Change URL, description, and summary; remove MANIFEST

* Wed Apr 21 2004 Stefan van der Eijk <stefan@eijk.nu> 0.11-1mdk
- initial package

