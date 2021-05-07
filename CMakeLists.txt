cmake_minimum_required(VERSION 3.15)
project(cmake_wrapper)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(KEEP_RPATHS)
set(CMAKE_SKIP_INSTALL_RPATH ON CACHE BOOL "CMAKE_SKIP_INSTALL_RPATH" FORCE)

add_subdirectory(src)
