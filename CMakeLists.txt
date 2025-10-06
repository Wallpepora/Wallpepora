cmake_minimum_required(VERSION 3.20)
project(Wallpepora LANGUAGES CXX)

# Force C++ 17 as the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find main dependencies
find_package(OpenCV REQUIRED)
find_package(Qt6 REQUIRED COMPONENTS Core Widgets)

# Project setup for Qt6
qt_standard_project_setup()

set(CMAKE_AUTORCC ON)

# Set the path to search for ui files
set(CMAKE_AUTOUIC_SEARCH_PATHS "${CMAKE_SOURCE_DIR}/ui")

# Include directories to find header files of OpenCV and the application
include_directories(${OpenCV_INCLUDE_DIRS} "${CMAKE_SOURCE_DIR}/include/")

# C++ source files
file(GLOB_RECURSE SRC_FILES "${CMAKE_SOURCE_DIR}/src/*.cpp")
message(STATUS "Sources files: ${SRC_FILES}")

# C++ headers
file(GLOB_RECURSE HEADERS "${CMAKE_SOURCE_DIR}/include/*.hpp")
message(STATUS "Headers: ${HEADERS}")

# Qt6 ui files
file(GLOB UI_FILES "${CMAKE_SOURCE_DIR}/ui/*.ui")
message(STATUS "Ui files: ${UI_FILES}")

# Main executable
add_executable(Wallpepora
    ${SRC_FILES}
    ${HEADERS}
    ${UI_FILES}
    ${CMAKE_SOURCE_DIR}/resources/resources.qrc
)
target_link_libraries(Wallpepora PRIVATE ${OpenCV_LIBS} Qt6::Core Qt6::Widgets)

# Find tests specific dependencies
find_package(GTest REQUIRED)

# Include directories to find header files of fixtures
include_directories("${CMAKE_SOURCE_DIR}/tests/fixtures/")

# C++ source files of the tests and fixtures
file(GLOB_RECURSE TESTS_SRC_FILES "${CMAKE_SOURCE_DIR}/tests/*.cpp")
message(STATUS "Tests sources files: ${TESTS_SRC_FILES}")

# Remove the file src/main.cpp in the list SRC_FILES 
# to avoid conflicts with the tests main
list(REMOVE_ITEM SRC_FILES "${CMAKE_SOURCE_DIR}/src/main.cpp")

# Tests executable
add_executable(Wallpepora_tests
    ${SRC_FILES}
    ${HEADERS}
    ${UI_FILES}
    ${CMAKE_SOURCE_DIR}/resources/resources.qrc
    ${TESTS_SRC_FILES}
)
target_link_libraries(Wallpepora_tests PRIVATE ${OpenCV_LIBS} Qt6::Core Qt6::Widgets GTest::gtest_main)