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
CMAKE_SOURCE_DIR = /home/alexie/Documents/slam_demo_TK/slam_demo

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/alexie/Documents/slam_demo_TK/slam_demo/cmake-build-debug

# Include any dependencies generated for this target.
include sim/sim_visualization/CMakeFiles/sim_opt_vis.dir/depend.make

# Include the progress variables for this target.
include sim/sim_visualization/CMakeFiles/sim_opt_vis.dir/progress.make

# Include the compile flags for this target's objects.
include sim/sim_visualization/CMakeFiles/sim_opt_vis.dir/flags.make

sim/sim_visualization/CMakeFiles/sim_opt_vis.dir/sim_opt_vis.cc.o: sim/sim_visualization/CMakeFiles/sim_opt_vis.dir/flags.make
sim/sim_visualization/CMakeFiles/sim_opt_vis.dir/sim_opt_vis.cc.o: ../sim/sim_visualization/sim_opt_vis.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/alexie/Documents/slam_demo_TK/slam_demo/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object sim/sim_visualization/CMakeFiles/sim_opt_vis.dir/sim_opt_vis.cc.o"
	cd /home/alexie/Documents/slam_demo_TK/slam_demo/cmake-build-debug/sim/sim_visualization && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/sim_opt_vis.dir/sim_opt_vis.cc.o -c /home/alexie/Documents/slam_demo_TK/slam_demo/sim/sim_visualization/sim_opt_vis.cc

sim/sim_visualization/CMakeFiles/sim_opt_vis.dir/sim_opt_vis.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/sim_opt_vis.dir/sim_opt_vis.cc.i"
	cd /home/alexie/Documents/slam_demo_TK/slam_demo/cmake-build-debug/sim/sim_visualization && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/alexie/Documents/slam_demo_TK/slam_demo/sim/sim_visualization/sim_opt_vis.cc > CMakeFiles/sim_opt_vis.dir/sim_opt_vis.cc.i

sim/sim_visualization/CMakeFiles/sim_opt_vis.dir/sim_opt_vis.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/sim_opt_vis.dir/sim_opt_vis.cc.s"
	cd /home/alexie/Documents/slam_demo_TK/slam_demo/cmake-build-debug/sim/sim_visualization && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/alexie/Documents/slam_demo_TK/slam_demo/sim/sim_visualization/sim_opt_vis.cc -o CMakeFiles/sim_opt_vis.dir/sim_opt_vis.cc.s

# Object files for target sim_opt_vis
sim_opt_vis_OBJECTS = \
"CMakeFiles/sim_opt_vis.dir/sim_opt_vis.cc.o"

# External object files for target sim_opt_vis
sim_opt_vis_EXTERNAL_OBJECTS =

sim/sim_visualization/sim_opt_vis: sim/sim_visualization/CMakeFiles/sim_opt_vis.dir/sim_opt_vis.cc.o
sim/sim_visualization/sim_opt_vis: sim/sim_visualization/CMakeFiles/sim_opt_vis.dir/build.make
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libboost_system.so
sim/sim_visualization/sim_opt_vis: lib/liblib.a
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_shape.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_aruco.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_bgsegm.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_bioinspired.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_ccalib.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_datasets.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_dpm.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_face.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_freetype.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_fuzzy.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_hdf.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_line_descriptor.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_optflow.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_video.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_plot.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_reg.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_saliency.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_stereo.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_structured_light.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_viz.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_phase_unwrapping.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_rgbd.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_surface_matching.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_text.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_ximgproc.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_xobjdetect.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_xphoto.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_videoio.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_imgcodecs.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libopencv_core.so.3.2.0
sim/sim_visualization/sim_opt_vis: /usr/local/lib/libceres.a
sim/sim_visualization/sim_opt_vis: /usr/lib/x86_64-linux-gnu/libglog.so
sim/sim_visualization/sim_opt_vis: sim/sim_visualization/CMakeFiles/sim_opt_vis.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/alexie/Documents/slam_demo_TK/slam_demo/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable sim_opt_vis"
	cd /home/alexie/Documents/slam_demo_TK/slam_demo/cmake-build-debug/sim/sim_visualization && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/sim_opt_vis.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
sim/sim_visualization/CMakeFiles/sim_opt_vis.dir/build: sim/sim_visualization/sim_opt_vis

.PHONY : sim/sim_visualization/CMakeFiles/sim_opt_vis.dir/build

sim/sim_visualization/CMakeFiles/sim_opt_vis.dir/clean:
	cd /home/alexie/Documents/slam_demo_TK/slam_demo/cmake-build-debug/sim/sim_visualization && $(CMAKE_COMMAND) -P CMakeFiles/sim_opt_vis.dir/cmake_clean.cmake
.PHONY : sim/sim_visualization/CMakeFiles/sim_opt_vis.dir/clean

sim/sim_visualization/CMakeFiles/sim_opt_vis.dir/depend:
	cd /home/alexie/Documents/slam_demo_TK/slam_demo/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/alexie/Documents/slam_demo_TK/slam_demo /home/alexie/Documents/slam_demo_TK/slam_demo/sim/sim_visualization /home/alexie/Documents/slam_demo_TK/slam_demo/cmake-build-debug /home/alexie/Documents/slam_demo_TK/slam_demo/cmake-build-debug/sim/sim_visualization /home/alexie/Documents/slam_demo_TK/slam_demo/cmake-build-debug/sim/sim_visualization/CMakeFiles/sim_opt_vis.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : sim/sim_visualization/CMakeFiles/sim_opt_vis.dir/depend

