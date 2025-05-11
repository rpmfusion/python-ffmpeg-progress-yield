# Created by pyp2rpm-3.3.7
%global pypi_name ffmpeg_progress_yield

Name:           python-ffmpeg-progress-yield
Version:        0.12.0
Release:        %autorelease
Summary:        Run an ffmpeg command with progress

License:        MIT
URL:            https://github.com/slhck/ffmpeg-progress-yield
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
# Nedded for tests
BuildRequires:  ffmpeg
BuildRequires:  python3dist(pytest)

%description
Run an ffmpeg command with its progress yielded.

%package -n     python3-ffmpeg-progress-yield
Summary:        %{summary}
%{?python_provide:%python_provide python3-ffmpeg-progress-yield}

%description -n python3-ffmpeg-progress-yield
Run an ffmpeg command with its progress yielded.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%{python3} test/test.py

%files -n python3-ffmpeg-progress-yield -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/ffmpeg-progress-yield

%changelog
%autochangelog

