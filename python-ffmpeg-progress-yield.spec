# Created by pyp2rpm-3.3.7
%global pypi_name ffmpeg-progress-yield
%global pypi_version 0.2.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
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
* Tue Jan 04 2022 Sérgio Basto <sergio@serjux.com> - 0.2.0-1
- Initial package.
