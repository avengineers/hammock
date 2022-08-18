#!/usr/bin/env python3

import os
from platform import system
from Test.utils import *


class TestMiniCProject:
    def test_clean_build_symbols(self):
        project_dir = "resources/mini_c_symbols"
        build_dir = f"{project_dir}/build"
        if "Windows" in system():
            binary = f"{build_dir}/mini_c.exe"
        else:
            binary = f"{build_dir}/mini_c"

        exit_code = cmake_configure(project_dir, build_dir)
        """CMake configure shall be successful."""
        assert exit_code == 0

        exit_code = cmake_build_target(build_dir, "clean")
        """CMake clean shall be successful."""
        assert exit_code == 0
        assert not os.path.isfile(f"{build_dir}/mockups.mockup")
        assert not os.path.isfile(binary)

        exit_code = exit_code = cmake_build_target(build_dir, "all")
        """CMake build shall create expected mockups and binary."""
        assert exit_code == 0
        assert os.path.isfile(f"{build_dir}/mockups.mockup")
        assert os.path.isfile(binary)

        exit_code = run_process([f"./{binary}"])
        """Built binary shall be executable"""
        assert exit_code == 0

    def test_clean_build_plink(self):
        project_dir = "resources/mini_c_plink"
        build_dir = f"{project_dir}/build"
        if "Windows" in system():
            binary = f"{build_dir}/mini_c.exe"
        else:
            binary = f"{build_dir}/mini_c"

        exit_code = run_process(["cmake", "-S", project_dir, "-B", build_dir, "-G", "Ninja"])
        """CMake configure shall be successful."""
        assert exit_code == 0

        exit_code = run_process(["cmake", "--build", build_dir, "--target", "clean"])
        """CMake clean shall be successful."""
        assert exit_code == 0
        assert not os.path.isfile(f"{build_dir}/mockups.mockup")
        assert not os.path.isfile(binary)

        exit_code = run_process(["cmake", "--build", build_dir])
        """CMake build shall create expected mockups and binary."""
        assert exit_code == 0
        assert os.path.isfile(f"{build_dir}/mockups.mockup")
        assert os.path.isfile(binary)

        exit_code = run_process([f"./{binary}"])
        """Built binary shall be executable"""
        assert exit_code == 3

    def test_build_and_test_with_gmock(self):
        project_dir = "resources/mini_c_gmock"
        build_dir = f"{project_dir}/build"
        if "Windows" in system():
            binary = f"{build_dir}/mini_c.exe"
        else:
            binary = f"{build_dir}/mini_c"

        exit_code = run_process(["cmake", "-S", project_dir, "-B", build_dir, "-G", "Ninja"])
        """CMake configure shall be successful."""
        assert exit_code == 0

        exit_code = run_process(["cmake", "--build", build_dir])
        """CMake build shall be successful."""
        assert exit_code == 0

        exit_code = run_process(["cmake", "--build", build_dir, "--target", "test"])
        """CMake test shall be successful."""
        assert exit_code == 0
