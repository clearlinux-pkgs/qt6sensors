#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
Name     : qt6sensors
Version  : 6.6.1
Release  : 4
URL      : https://download.qt.io/official_releases/qt/6.6/6.6.1/submodules/qtsensors-everywhere-src-6.6.1.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.6/6.6.1/submodules/qtsensors-everywhere-src-6.6.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qt6sensors-lib = %{version}-%{release}
Requires: qt6sensors-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : mesa-dev
BuildRequires : pkg-config
BuildRequires : qt6base-dev
BuildRequires : qt6declarative-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the qt6sensors package.
Group: Development
Requires: qt6sensors-lib = %{version}-%{release}
Provides: qt6sensors-devel = %{version}-%{release}
Requires: qt6sensors = %{version}-%{release}

%description dev
dev components for the qt6sensors package.


%package lib
Summary: lib components for the qt6sensors package.
Group: Libraries
Requires: qt6sensors-license = %{version}-%{release}

%description lib
lib components for the qt6sensors package.


%package license
Summary: license components for the qt6sensors package.
Group: Default

%description license
license components for the qt6sensors package.


%prep
%setup -q -n qtsensors-everywhere-src-6.6.1
cd %{_builddir}/qtsensors-everywhere-src-6.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1703009275
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1703009275
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6sensors
cp %{_builddir}/qtsensors-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6sensors/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qtsensors-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt6sensors/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qtsensors-everywhere-src-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qt6sensors/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/qtsensors-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6sensors/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qtsensors-everywhere-src-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6sensors/f45ee1c765646813b442ca58de72e20a64a7ddba || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/metatypes/qt6sensors_relwithdebinfo_metatypes.json
/usr/lib64/qt6/mkspecs/modules/qt_lib_sensors.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_sensors_private.pri
/usr/lib64/qt6/modules/Sensors.json

%files dev
%defattr(-,root,root,-)
/usr/include/QtSensors/6.6.1/QtSensors/private/qaccelerometer_p.h
/usr/include/QtSensors/6.6.1/QtSensors/private/qambientlightsensor_p.h
/usr/include/QtSensors/6.6.1/QtSensors/private/qambienttemperaturesensor_p.h
/usr/include/QtSensors/6.6.1/QtSensors/private/qcompass_p.h
/usr/include/QtSensors/6.6.1/QtSensors/private/qgyroscope_p.h
/usr/include/QtSensors/6.6.1/QtSensors/private/qhumiditysensor_p.h
/usr/include/QtSensors/6.6.1/QtSensors/private/qirproximitysensor_p.h
/usr/include/QtSensors/6.6.1/QtSensors/private/qlidsensor_p.h
/usr/include/QtSensors/6.6.1/QtSensors/private/qlightsensor_p.h
/usr/include/QtSensors/6.6.1/QtSensors/private/qmagnetometer_p.h
/usr/include/QtSensors/6.6.1/QtSensors/private/qorientationsensor_p.h
/usr/include/QtSensors/6.6.1/QtSensors/private/qpressuresensor_p.h
/usr/include/QtSensors/6.6.1/QtSensors/private/qproximitysensor_p.h
/usr/include/QtSensors/6.6.1/QtSensors/private/qrotationsensor_p.h
/usr/include/QtSensors/6.6.1/QtSensors/private/qsensor_p.h
/usr/include/QtSensors/6.6.1/QtSensors/private/qtapsensor_p.h
/usr/include/QtSensors/6.6.1/QtSensors/private/qtiltsensor_p.h
/usr/include/QtSensors/6.6.1/QtSensors/private/qtsensors-config_p.h
/usr/include/QtSensors/6.6.1/QtSensors/private/sensorlog_p.h
/usr/include/QtSensors/QAccelerometer
/usr/include/QtSensors/QAccelerometerFilter
/usr/include/QtSensors/QAccelerometerReading
/usr/include/QtSensors/QAmbientLightFilter
/usr/include/QtSensors/QAmbientLightReading
/usr/include/QtSensors/QAmbientLightSensor
/usr/include/QtSensors/QAmbientTemperatureFilter
/usr/include/QtSensors/QAmbientTemperatureReading
/usr/include/QtSensors/QAmbientTemperatureSensor
/usr/include/QtSensors/QCompass
/usr/include/QtSensors/QCompassFilter
/usr/include/QtSensors/QCompassReading
/usr/include/QtSensors/QGyroscope
/usr/include/QtSensors/QGyroscopeFilter
/usr/include/QtSensors/QGyroscopeReading
/usr/include/QtSensors/QHumidityFilter
/usr/include/QtSensors/QHumidityReading
/usr/include/QtSensors/QHumiditySensor
/usr/include/QtSensors/QIRProximityFilter
/usr/include/QtSensors/QIRProximityReading
/usr/include/QtSensors/QIRProximitySensor
/usr/include/QtSensors/QLidFilter
/usr/include/QtSensors/QLidReading
/usr/include/QtSensors/QLidSensor
/usr/include/QtSensors/QLightFilter
/usr/include/QtSensors/QLightReading
/usr/include/QtSensors/QLightSensor
/usr/include/QtSensors/QMagnetometer
/usr/include/QtSensors/QMagnetometerFilter
/usr/include/QtSensors/QMagnetometerReading
/usr/include/QtSensors/QOrientationFilter
/usr/include/QtSensors/QOrientationReading
/usr/include/QtSensors/QOrientationSensor
/usr/include/QtSensors/QPressureFilter
/usr/include/QtSensors/QPressureReading
/usr/include/QtSensors/QPressureSensor
/usr/include/QtSensors/QProximityFilter
/usr/include/QtSensors/QProximityReading
/usr/include/QtSensors/QProximitySensor
/usr/include/QtSensors/QRotationFilter
/usr/include/QtSensors/QRotationReading
/usr/include/QtSensors/QRotationSensor
/usr/include/QtSensors/QSensor
/usr/include/QtSensors/QSensorBackend
/usr/include/QtSensors/QSensorBackendFactory
/usr/include/QtSensors/QSensorChangesInterface
/usr/include/QtSensors/QSensorFilter
/usr/include/QtSensors/QSensorManager
/usr/include/QtSensors/QSensorPluginInterface
/usr/include/QtSensors/QSensorReading
/usr/include/QtSensors/QTapFilter
/usr/include/QtSensors/QTapReading
/usr/include/QtSensors/QTapSensor
/usr/include/QtSensors/QTiltFilter
/usr/include/QtSensors/QTiltReading
/usr/include/QtSensors/QTiltSensor
/usr/include/QtSensors/QtSensors
/usr/include/QtSensors/QtSensorsDepends
/usr/include/QtSensors/QtSensorsVersion
/usr/include/QtSensors/qaccelerometer.h
/usr/include/QtSensors/qambientlightsensor.h
/usr/include/QtSensors/qambienttemperaturesensor.h
/usr/include/QtSensors/qcompass.h
/usr/include/QtSensors/qgyroscope.h
/usr/include/QtSensors/qhumiditysensor.h
/usr/include/QtSensors/qirproximitysensor.h
/usr/include/QtSensors/qlidsensor.h
/usr/include/QtSensors/qlightsensor.h
/usr/include/QtSensors/qmagnetometer.h
/usr/include/QtSensors/qorientationsensor.h
/usr/include/QtSensors/qpressuresensor.h
/usr/include/QtSensors/qproximitysensor.h
/usr/include/QtSensors/qrotationsensor.h
/usr/include/QtSensors/qsensor.h
/usr/include/QtSensors/qsensorbackend.h
/usr/include/QtSensors/qsensormanager.h
/usr/include/QtSensors/qsensorplugin.h
/usr/include/QtSensors/qsensorsglobal.h
/usr/include/QtSensors/qtapsensor.h
/usr/include/QtSensors/qtiltsensor.h
/usr/include/QtSensors/qtsensors-config.h
/usr/include/QtSensors/qtsensorsexports.h
/usr/include/QtSensors/qtsensorsversion.h
/usr/lib64/cmake/Qt6/FindSensorfw.cmake
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtSensorsTestsConfig.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6IIOSensorProxySensorPluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6IIOSensorProxySensorPluginConfig.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6IIOSensorProxySensorPluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6IIOSensorProxySensorPluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6IIOSensorProxySensorPluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6IIOSensorProxySensorPluginTargets.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6SensorsAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6SensorsConfig.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6SensorsConfigVersion.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6SensorsConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6SensorsDependencies.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6SensorsPlugins.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6SensorsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6SensorsTargets.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6SensorsVersionlessTargets.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6genericSensorPluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6genericSensorPluginConfig.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6genericSensorPluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6genericSensorPluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6genericSensorPluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Sensors/Qt6genericSensorPluginTargets.cmake
/usr/lib64/libQt6Sensors.prl
/usr/lib64/libQt6Sensors.so
/usr/lib64/pkgconfig/Qt6Sensors.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt6Sensors.so.6
/usr/lib64/libQt6Sensors.so.6.6.1
/usr/lib64/qt6/plugins/sensors/libqtsensors_generic.so
/usr/lib64/qt6/plugins/sensors/libqtsensors_iio-sensor-proxy.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6sensors/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qt6sensors/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt6sensors/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt6sensors/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
/usr/share/package-licenses/qt6sensors/f45ee1c765646813b442ca58de72e20a64a7ddba
