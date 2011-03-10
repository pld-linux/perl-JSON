#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	JSON
Summary:	JSON - parse and convert to JSON (JavaScript Object Notation)
Summary(pl.UTF-8):	JSON - analiza i konwersja do notacji JSON (JavaScript Object Notation)
Name:		perl-JSON
Version:	2.51
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MAKAMAKA/%{pdir}-%{version}.tar.gz
# Source0-md5:	d0ead26851f1e84d122f34533c3809cc
URL:		http://search.cpan.org/dist/JSON/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Suggests:	perl-JSON-XS
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module converts between JSON (JavaScript Object Notation) and
Perl data structure into each other.

For JSON, See to <http://www.crockford.com/JSON/>.

%description -l pl.UTF-8
Ten moduł dokonuje konwersji między notacją JSON (JavaScript Object
Notation) a perlowymi strukturami danych.

Więcej informacji na temat notacji JSON można znaleźć pod adresem
<http://www.crockford.com/JSON/>.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/JSON
%{_mandir}/man3/*
