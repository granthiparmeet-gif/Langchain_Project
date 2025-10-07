cmake -B build -G "Ninja" ^
    -DCMAKE_BUILD_TYPE=Release ^
    -DCMAKE_INSTALL_PREFIX="%LIBRARY_PREFIX%" ^
    -DBUILD_SHARED_LIBS=ON ^
    -DIMPORT_LIB_SUFFIX:STRING="" ^
    -DBUILD_STATIC_LIBS=OFF ^
    -DCURL_STATICLIB=OFF ^
    -DCURL_USE_SCHANNEL=ON ^
    -DCURL_ZLIB=ON ^
    -DCURL_USE_SSH=ON ^
    -DUSE_NGHTTP2=ON ^
    -DBUILD_TESTING=ON ^
    -DBUILD_CURL_EXE=ON ^
    -DENABLE_IDN=OFF ^
    -DCURL_WINDOWS_SSPI=ON ^
    -DENABLE_UNICODE=ON ^
    -DCURL_USE_LIBPSL=OFF ^
    -DCURL_DISABLE_LDAP=ON ^
    -DCURL_ZSTD=ON

cmake --build build --config Release

cd build
ctest --output-on-failure -j${CPU_COUNT}
cd ..

cmake --install build

if errorlevel 1 exit 1
:: Includes man pages and other miscellaneous.
rm -rf %LIBRARY_PREFIX%\share
exit 0

