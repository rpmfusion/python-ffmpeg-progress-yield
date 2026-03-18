Name:           python-ffmpeg-progress-yield
Version:        1.1.2
Release:        %autorelease
Summary:        Run an ffmpeg command with progress

License:        MIT
URL:            https://github.com/slhck/ffmpeg-progress-yield
Source0:        %{url}/archive/refs/tags/v%{version}/ffmpeg-progress-yield-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# Nedded for tests
BuildRequires:  ffmpeg
BuildRequires:  procps-ng
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)

%description
Run an ffmpeg command with its progress yielded.

%package -n     python3-ffmpeg-progress-yield
Summary:        %{summary}
Recommends:     %{_bindir}/ffmpeg

%description -n python3-ffmpeg-progress-yield
Run an ffmpeg command with its progress yielded.

%prep
%autosetup -p1 -n ffmpeg-progress-yield-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l ffmpeg_progress_yield

%check
%{pytest} tests/test_ffmpeg_progress.py

%files -n python3-ffmpeg-progress-yield -f %{pyproject_files}
%license LICENSE.md
%doc README.md
%{_bindir}/ffmpeg-progress-yield

%changelog
%autochangelog

