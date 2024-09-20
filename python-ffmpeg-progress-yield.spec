# Created by pyp2rpm-3.3.7
%global pypi_name ffmpeg-progress-yield
%global pypi_version 0.7.9

Name:           python-%{pypi_name}
Version:        0.9.1
Release:        1%{?dist}
Summary:        Run an ffmpeg command with progress

License:        MIT
URL:            https://github.com/slhck/ffmpeg-progress-yield
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Run an ffmpeg command with its progress yielded.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
Run an ffmpeg command with its progress yielded.


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/ffmpeg-progress-yield
%{python3_sitelib}/ffmpeg_progress_yield
%{python3_sitelib}/ffmpeg_progress_yield-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Fri Sep 20 2024 Leigh Scott <leigh123linux@gmail.com> - 0.9.1-1
- Update to 0.9.1

* Sun Aug 18 2024 Leigh Scott <leigh123linux@gmail.com> - 0.7.9-1
- Update to 0.7.9

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.7.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 13 2024 Leigh Scott <leigh123linux@gmail.com> - 0.7.8-5
- Rebuilt for Python 3.13

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.7.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.7.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Leigh Scott <leigh123linux@gmail.com> - 0.7.8-2
- Rebuilt for Python 3.12

* Sun Jul 02 2023 Leigh Scott <leigh123linux@gmail.com> - 0.7.8-1
- Update to 0.7.8

* Sun May 07 2023 Leigh Scott <leigh123linux@gmail.com> - 0.7.4-1
- Update to 0.7.4

* Wed Mar 15 2023 Leigh Scott <leigh123linux@gmail.com> - 0.7.2-1
- Update to 0.7.2

* Fri Feb 10 2023 Leigh Scott <leigh123linux@gmail.com> - 0.7.0-1
- Update to 0.7.0

* Tue Dec 20 2022 Leigh Scott <leigh123linux@gmail.com> - 0.6.1-1
- Update to 0.6.1

* Thu Dec 15 2022 Leigh Scott <leigh123linux@gmail.com> - 0.5.0-1
- Update to 0.5.0

* Sun Dec 11 2022 Leigh Scott <leigh123linux@gmail.com> - 0.4.0-1
- Update to 0.4.0

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Aug 04 2022 Leigh Scott <leigh123linux@gmail.com> - 0.3.0-1
- Update to 0.3.0

* Sat Jun 25 2022 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-2
- Rebuilt for Python 3.11

* Tue Jan 04 2022 Sérgio Basto <sergio@serjux.com> - 0.2.0-1
- Initial package.
