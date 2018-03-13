# Copyright: Universidad Carlos III de Madrid (C) 2016;
# Authors: Raul Fernandez-Fernandez, Juan G. Victores
# CopyPolicy: Released under the terms of the GNU GPL v2.0.

cmake_minimum_required(VERSION 2.6)

project(TEO_OPENRAVE_MODELS)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake)

add_subdirectory(openrave)

include(GNUInstallDirs)

if(WIN32 AND NOT CYGWIN)
    set(_cmake_destination CMake)
else()
    set(_cmake_destination ${CMAKE_INSTALL_LIBDIR}/cmake/TEO_OPENRAVE_MODELS)
endif()

export(PACKAGE TEO_OPENRAVE_MODELS)

file(WRITE ${CMAKE_BINARY_DIR}/TEO_OPENRAVE_MODELSConfig.cmake "# Dummy CMake configuration export file.")
install(FILES ${CMAKE_BINARY_DIR}/TEO_OPENRAVE_MODELSConfig.cmake DESTINATION ${_cmake_destination})

# uninstall target
configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/cmake/template/TEO_OPENRAVE_MODELSConfigUninstall.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/TEO_OPENRAVE_MODELSConfigUninstall.cmake" IMMEDIATE @ONLY)

add_custom_target(uninstall
    COMMAND ${CMAKE_COMMAND} -P ${CMAKE_CURRENT_BINARY_DIR}/TEO_OPENRAVE_MODELSConfigUninstall.cmake)
