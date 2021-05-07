from conans import ConanFile, CMake, tools
import os, shutil


class RtAudioConan(ConanFile):
    name = "rtaudio"
    license = "MIT"
    description = "A set of C++ classes that provide a common API for realtime audio input/output across Linux (native ALSA, JACK, PulseAudio and OSS), Macintosh OS X (CoreAudio and JACK), and Windows (DirectSound, ASIO, and WASAPI) operating systems"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "direct_sound": [True, False],
        "asio": [True, False],
        "wasapi": [True, False],
        "alsa": [True, False],
        "pulse": [True, False],
        "jack": [True, False],
        "core": [True, False],
    }
    default_options = {
        "shared": True,
        "fPIC": True,
        "direct_sound": False,
        "asio": False,
        "wasapi": True,
        "alsa": True,
        "pulse": False,
        "jack": False,
        "core": True,
    }
    exports_sources = "CMakeLists.txt"
    no_copy_source = True
    generators = "cmake"

    def configure(self):
        if not tools.os_info.is_windows:
            del self.options.direct_sound
            del self.options.asio
            del self.options.wasapi
        if not tools.os_info.is_linux:
            del self.options.alsa
            del self.options.pulse
            del self.options.jack
        if not tools.os_info.is_macos:
            del self.options.core


    def requirements(self):
        if "alsa" in self.options and self.options.alsa:
            self.requires("libalsa/1.1.5@conan/stable")
            # self.requires("libalsa/1.1.9")
            # self.requires("libalsa/1.2.2")

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        os.rename("rtaudio-%s" % self.version, "src")
        tools.replace_in_file(
            os.path.join("src", "CMakeLists.txt"),
            'cmake_policy(SET CMP0042 OLD)',
            '',
        )

    def build(self):
        cmake = CMake(self)
        defs = {
            "BUILD_TESTING": False,
            "RTAUDIO_API_DS": "direct_sound" in self.options and self.options.direct_sound,
            "RTAUDIO_API_ASIO": "asio" in self.options and self.options.asio,
            "RTAUDIO_API_WASAPI": "wasapi" in self.options and self.options.wasapi,
            "RTAUDIO_API_ALSA": "alsa" in self.options and self.options.alsa,
            "RTAUDIO_API_PULSE": "pulse" in self.options and self.options.pulse,
            "RTAUDIO_API_JACK": "jack" in self.options and self.options.jack,
            "RTAUDIO_API_CORE": "core" in self.options and self.options.core,
        }
        cmake.configure(defs=defs)
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        for p in ["cmake_find_package", "cmake_find_package_multi"]:
            self.cpp_info.names[p] = "RtAudio"
