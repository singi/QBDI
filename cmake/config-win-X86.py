import subprocess

subprocess.check_call(["cmake", "..",
                       "-G", "Visual Studio 14 2015",
                       "-DCMAKE_CXX_FLAGS=/D_SILENCE_TR1_NAMESPACE_DEPRECATION_WARNING",
                       "-DCMAKE_BUILD_TYPE=Release",
                       "-DCMAKE_CROSSCOMPILING=FALSE",
                       "-DPLATFORM=win-X86"])
