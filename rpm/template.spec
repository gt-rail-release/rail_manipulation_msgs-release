Name:           ros-indigo-rail-manipulation-msgs
Version:        0.0.7
Release:        0%{?dist}
Summary:        ROS rail_manipulation_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rail_manipulation_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-visualization-msgs

%description
Common Manipulation Messages and Services Used in RAIL Manipulation Packages

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Apr 27 2015 David Kent <davidkent@wpi.edu> - 0.0.7-0
- Autogenerated by Bloom

* Wed Apr 22 2015 David Kent <davidkent@wpi.edu> - 0.0.6-0
- Autogenerated by Bloom

* Tue Apr 14 2015 David Kent <davidkent@wpi.edu> - 0.0.5-0
- Autogenerated by Bloom

* Fri Apr 10 2015 David Kent <davidkent@wpi.edu> - 0.0.4-0
- Autogenerated by Bloom

* Tue Mar 31 2015 David Kent <davidkent@wpi.edu> - 0.0.3-0
- Autogenerated by Bloom

* Tue Mar 24 2015 David Kent <davidkent@wpi.edu> - 0.0.2-0
- Autogenerated by Bloom

* Tue Mar 24 2015 David Kent <davidkent@wpi.edu> - 0.0.1-0
- Autogenerated by Bloom

