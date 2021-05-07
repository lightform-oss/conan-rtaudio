project(PackageTest CXX)
cmake_minimum_required(VERSION 3.15)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(KEEP_RPATHS)
set(CMAKE_SKIP_INSTALL_RPATH ON CACHE BOOL "CMAKE_SKIP_INSTALL_RPATH" FORCE)

set(CMAKE_VERBOSE_MAKEFILE ON)

add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS})

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
