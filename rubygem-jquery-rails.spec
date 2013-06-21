%global gem_name jquery-rails
%if 0%{?rhel} == 6
%global gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}
%global gem_cache %{gem_dir}/cache/%{gem_name}-%{version}.gem
%global gem_spec %{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%endif

Summary: Use jQuery with Rails 3
Name: rubygem-%{gem_name}
Epoch: 1
Version: 2.0.3
Release: 3%{?dist}
Group: Development/Languages
# jquery-rails itself is MIT, bundled JavaScripts are the rest
License: MIT and (MIT or GPLv2) and (MIT or BSD or GPLv2) and BSD
URL: http://rubygems.org/gems/jquery-rails
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
%if 0%{?rhel} == 6 || 0%{?fedora} < 17
Requires: ruby(abi) = 1.8
%else
Requires: ruby(abi) = 1.9.1
%endif
Requires: ruby(rubygems)
Requires: rubygem(railties) >= 3.0
Requires: rubygem(railties) < 4
Requires: rubygem(thor) => 0.14
Requires: rubygem(thor) < 1
%if 0%{?fedora}
BuildRequires: rubygems-devel
%endif
BuildRequires: rubygems >= 1.8
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
This gem provides jQuery and the jQuery-ujs driver for your Rails 3
application.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# no tests :(
# see https://github.com/rails/jquery-rails/pull/56
# rspec spec
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
# bunch of bundled JS files here
%{gem_instdir}/vendor
%{gem_instdir}/lib
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/Gemfile
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
#_mx %doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.lock
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/README.md
#_mx %{gem_instdir}/spec

%changelog
* Fri Jun 07 2013 Sergey Mihailov <sergey.mihailov@gmail.com> - 2.0.3-3
- Update release

* Mon Nov 05 2012 Ivan Necas <inecas@redhat.com> 1.0.19-5
- 873195 - build with newer version of rubygems (inecas@redhat.com)

* Fri Aug 10 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.19-4
- rhel6 do not know gem_libdir (msuchy@redhat.com)

* Fri Aug 10 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.19-3
- add rubygems to buildrequires (msuchy@redhat.com)

* Fri Aug 10 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.19-2
- new package built with tito

* Mon Jul 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.0.2-1
- Initial package
