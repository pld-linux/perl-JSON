#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	JSON
Summary:	JSON - parse and convert to JSON (JavaScript Object Notation).
#Summary(pl.UTF-8):	
Name:		perl-JSON
Version:	1.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MA/MAKAMAKA/JSON-1.07.tar.gz
# Source0-md5:	c7b385e35f37b4c8595c4f6e7eeb573e
URL:		http://search.cpan.org/dist/JSON/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Response)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module converts between JSON (JavaScript Object Notation) and Perl
data structure into each other.

For JSON, See to http://www.crockford.com/JSON/.

# %description -l pl.UTF-8
# TODO

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
%{perl_vendorlib}/Apache/*.pm
%{perl_vendorlib}/JSON/
%{perl_vendorlib}/JSONRPC/
%{_mandir}/man3/*
