

set -ex



test -f $PREFIX/lib/libc++.1.dylib
test ! -L $PREFIX/lib/libc++.dylib
test ! -d $PREFIX/include/c++
test ! -f $PREFIX/lib/libc++.a
exit 0
