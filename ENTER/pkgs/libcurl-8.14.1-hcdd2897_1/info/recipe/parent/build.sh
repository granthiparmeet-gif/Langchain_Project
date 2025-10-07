#!/bin/bash
set -ex

export CFLAGS="$CFLAGS $CPPFLAGS"

if [[ "$target_platform" == "osx-"* ]]; then
    SSL_OPTIONS="-DCURL_USE_OPENSSL=ON -DCURL_USE_SECTRANSP=ON"
else
    SSL_OPTIONS="-DCURL_USE_OPENSSL=ON"
fi

# Configure the build with CMake
cmake -S . -B build \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=${PREFIX} \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_STATIC_LIBS=OFF \
    -DCURL_STATICLIB=OFF \
    -DCURL_CA_BUNDLE=${PREFIX}/ssl/cacert.pem \
    ${SSL_OPTIONS} \
    -DCURL_ZLIB=ON \
    -DCURL_USE_SSH=ON \
    -DUSE_NGHTTP2=ON \
    -DBUILD_TESTING=ON \
    -DBUILD_CURL_EXE=ON \
    -DCURL_USE_LIBPSL=OFF \
    -DCURL_DISABLE_LDAP=ON \
    -DCURL_ZSTD=ON \
    -DCURL_GSSAPI=ON \
    -DCURL_USE_LIBSSH2=ON

cmake --build build --parallel ${CPU_COUNT} --verbose

cd build
ctest --output-on-failure -j${CPU_COUNT} \
    -E "(1173|1139|971|1705|1706)"
cd ..

cmake --install build

# Includes man pages and other miscellaneous.
rm -rf "${PREFIX}/share"

