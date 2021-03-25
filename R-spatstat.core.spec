#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-spatstat.core
Version  : 2.0.0
Release  : 2
URL      : https://cran.r-project.org/src/contrib/spatstat.core_2.0-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/spatstat.core_2.0-0.tar.gz
Summary  : Core Functionality of the 'spatstat' Family
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-spatstat.core-lib = %{version}-%{release}
Requires: R-abind
Requires: R-goftest
Requires: R-spatstat.data
Requires: R-spatstat.geom
Requires: R-spatstat.sparse
Requires: R-spatstat.utils
Requires: R-tensor
BuildRequires : R-abind
BuildRequires : R-goftest
BuildRequires : R-spatstat.data
BuildRequires : R-spatstat.geom
BuildRequires : R-spatstat.sparse
BuildRequires : R-spatstat.utils
BuildRequires : R-tensor
BuildRequires : buildreq-R

%description
spatial data, mainly spatial point patterns,
	     in the 'spatstat' family of packages.
	     (Excludes analysis of spatial data on a linear network,
	     which is covered by the separate package 'spatstat.linnet'.)
	     Exploratory methods include quadrat counts, K-functions and their simulation envelopes, nearest neighbour distance and empty space statistics, Fry plots, pair correlation function, kernel smoothed intensity, relative risk estimation with cross-validated bandwidth selection, mark correlation functions, segregation indices, mark dependence diagnostics, and kernel estimates of covariate effects. Formal hypothesis tests of random pattern (chi-squared, Kolmogorov-Smirnov, Monte Carlo, Diggle-Cressie-Loosmore-Ford, Dao-Genton, two-stage Monte Carlo) and tests for covariate effects (Cox-Berman-Waller-Lawson, Kolmogorov-Smirnov, ANOVA) are also supported.
	Parametric models can be fitted to point pattern data using the functions ppm(), kppm(), slrm(), dppm() similar to glm(). Types of models include Poisson, Gibbs and Cox point processes, Neyman-Scott cluster processes, and determinantal point processes. Models may involve dependence on covariates, inter-point interaction, cluster formation and dependence on marks. Models are fitted by maximum likelihood, logistic regression, minimum contrast, and composite likelihood methods. 
	A model can be fitted to a list of point patterns (replicated point pattern data) using the function mppm(). The model can include random effects and fixed effects depending on the experimental design, in addition to all the features listed above.
	Fitted point process models can be simulated, automatically. Formal hypothesis tests of a fitted model are supported (likelihood ratio test, analysis of deviance, Monte Carlo tests) along with basic tools for model selection (stepwise(), AIC()) and variable selection (sdr). Tools for validating the fitted model include simulation envelopes, residuals, residual plots and Q-Q plots, leverage and influence diagnostics, partial residuals, and added variable plots.

%package lib
Summary: lib components for the R-spatstat.core package.
Group: Libraries

%description lib
lib components for the R-spatstat.core package.


%prep
%setup -q -c -n spatstat.core
cd %{_builddir}/spatstat.core

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1616688673

%install
export SOURCE_DATE_EPOCH=1616688673
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spatstat.core
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spatstat.core
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spatstat.core
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc spatstat.core || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/spatstat.core/CITATION
/usr/lib64/R/library/spatstat.core/DESCRIPTION
/usr/lib64/R/library/spatstat.core/INDEX
/usr/lib64/R/library/spatstat.core/Meta/Rd.rds
/usr/lib64/R/library/spatstat.core/Meta/features.rds
/usr/lib64/R/library/spatstat.core/Meta/hsearch.rds
/usr/lib64/R/library/spatstat.core/Meta/links.rds
/usr/lib64/R/library/spatstat.core/Meta/nsInfo.rds
/usr/lib64/R/library/spatstat.core/Meta/package.rds
/usr/lib64/R/library/spatstat.core/NAMESPACE
/usr/lib64/R/library/spatstat.core/NEWS
/usr/lib64/R/library/spatstat.core/R/spatstat.core
/usr/lib64/R/library/spatstat.core/R/spatstat.core.rdb
/usr/lib64/R/library/spatstat.core/R/spatstat.core.rdx
/usr/lib64/R/library/spatstat.core/R/sysdata.rdb
/usr/lib64/R/library/spatstat.core/R/sysdata.rdx
/usr/lib64/R/library/spatstat.core/doc/packagesizes.txt
/usr/lib64/R/library/spatstat.core/help/AnIndex
/usr/lib64/R/library/spatstat.core/help/aliases.rds
/usr/lib64/R/library/spatstat.core/help/macros/defns.Rd
/usr/lib64/R/library/spatstat.core/help/paths.rds
/usr/lib64/R/library/spatstat.core/help/spatstat.core.rdb
/usr/lib64/R/library/spatstat.core/help/spatstat.core.rdx
/usr/lib64/R/library/spatstat.core/html/00Index.html
/usr/lib64/R/library/spatstat.core/html/R.css
/usr/lib64/R/library/spatstat.core/tests/testsAtoC.R
/usr/lib64/R/library/spatstat.core/tests/testsD.R
/usr/lib64/R/library/spatstat.core/tests/testsEtoF.R
/usr/lib64/R/library/spatstat.core/tests/testsGtoJ.R
/usr/lib64/R/library/spatstat.core/tests/testsK.R
/usr/lib64/R/library/spatstat.core/tests/testsL.R
/usr/lib64/R/library/spatstat.core/tests/testsM.R
/usr/lib64/R/library/spatstat.core/tests/testsNtoO.R
/usr/lib64/R/library/spatstat.core/tests/testsP1.R
/usr/lib64/R/library/spatstat.core/tests/testsP2.R
/usr/lib64/R/library/spatstat.core/tests/testsQ.R
/usr/lib64/R/library/spatstat.core/tests/testsR1.R
/usr/lib64/R/library/spatstat.core/tests/testsR2.R
/usr/lib64/R/library/spatstat.core/tests/testsS.R
/usr/lib64/R/library/spatstat.core/tests/testsT.R
/usr/lib64/R/library/spatstat.core/tests/testsUtoZ.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/spatstat.core/libs/spatstat.core.so
/usr/lib64/R/library/spatstat.core/libs/spatstat.core.so.avx2
/usr/lib64/R/library/spatstat.core/libs/spatstat.core.so.avx512
