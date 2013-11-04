%global packname  fit.models
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.5.10
Release:          1
Summary:          fit.models
Group:            Sciences/Mathematics
License:          GPLv1+
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-10.tar.gz
BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice 

Requires:         R-MASS 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-lattice

BuildRequires:   R-MASS 
%description
A framework for comparing fitted models

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
