# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.17

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/clion-2020.3.1/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /opt/clion-2020.3.1/bin/cmake/linux/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/alexie/Documents/slam_demo_TK/slam_demo/sim

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/alexie/Documents/slam_demo_TK/slam_demo/sim/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/sim_boem_app.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/sim_boem_app.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/sim_boem_app.dir/flags.make

CMakeFiles/sim_boem_app.dir/sim_boem_app.o: CMakeFiles/sim_boem_app.dir/flags.make
CMakeFiles/sim_boem_app.dir/sim_boem_app.o: ../sim_boem_app.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/alexie/Documents/slam_demo_TK/slam_demo/sim/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/sim_boem_app.dir/sim_boem_app.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/sim_boem_app.dir/sim_boem_app.o -c /home/alexie/Documents/slam_demo_TK/slam_demo/sim/sim_boem_app.cc

CMakeFiles/sim_boem_app.dir/sim_boem_app.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/sim_boem_app.dir/sim_boem_app.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/alexie/Documents/slam_demo_TK/slam_demo/sim/sim_boem_app.cc > CMakeFiles/sim_boem_app.dir/sim_boem_app.i

CMakeFiles/sim_boem_app.dir/sim_boem_app.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/sim_boem_app.dir/sim_boem_app.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/alexie/Documents/slam_demo_TK/slam_demo/sim/sim_boem_app.cc -o CMakeFiles/sim_boem_app.dir/sim_boem_app.s

# Object files for target sim_boem_app
sim_boem_app_OBJECTS = \
"CMakeFiles/sim_boem_app.dir/sim_boem_app.o"

# External object files for target sim_boem_app
sim_boem_app_EXTERNAL_OBJECTS =

sim_boem_app: CMakeFiles/sim_boem_app.dir/sim_boem_app.o
sim_boem_app: CMakeFiles/sim_boem_app.dir/build.make
sim_boem_app: CMakeFiles/sim_boem_app.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/alexie/Documents/slam_demo_TK/slam_demo/sim/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable sim_boem_app"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/sim_boem_app.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/sim_boem_app.dir/build: sim_boem_app

.PHONY : CMakeFiles/sim_boem_app.dir/build

CMakeFiles/sim_boem_app.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/sim_boem_app.dir/cmake_clean.cmake
.PHONY : CMakeFiles/sim_boem_app.dir/clean

CMakeFiles/sim_boem_app.dir/depend:
	cd /home/alexie/Documents/slam_demo_TK/slam_demo/sim/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/alexie/Documents/slam_demo_TK/slam_demo/sim /home/alexie/Documents/slam_demo_TK/slam_demo/sim /home/alexie/Documents/slam_demo_TK/slam_demo/sim/cmake-build-debug /home/alexie/Documents/slam_demo_TK/slam_demo/sim/cmake-build-debug /home/alexie/Documents/slam_demo_TK/slam_demo/sim/cmake-build-debug/CMakeFiles/sim_boem_app.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/sim_boem_app.dir/depend

