# CMake needs this line
cmake_minimum_required(VERSION 3.1)

# Enable C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

# Define project name
project(obj_detect)

# Find OpenCV, you may need to set OpenCV_DIR variable
# to the absolute path to the directory containing OpenCVConfig.cmake file
# via the command line or GUI
find_package(OpenCV REQUIRED PATHS "/home/preethamj/install-opencv")

# If the package has been found, several variables will
# be set, you can find the full list with descriptions
# in the OpenCVConfig.cmake file.
# Print some message showing some of them
message(STATUS "OpenCV library status:")
message(STATUS "    config: ${OpenCV_DIR}")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")


add_executable(obj_detect src/obj_detect.cpp)
include_directories( ${OpenCV_INCLUDE_DIRS} ${CMAKE_CURRENT_LIST_DIR}/include)
link_directories( ${OpenCV_LIB_DIR} )
target_link_libraries( obj_detect ${OpenCV_LIBS} )

#add_library(obj_detect SHARED src/obj_detect.cpp)
# target_link_libraries(obj_detect ${OpenCV_LIBS} ${CMAKE_CURRENT_LIST_DIR}/include)
#target_include_directories(obj_detect ${CMAKE_CURRENT_LIST_DIR}/include)
