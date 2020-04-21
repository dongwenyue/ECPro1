import jpype
import os

from ..configures.paths import CLASSPATH, RRSOURCE, JVMPATH
from ..platform.osutils import isWindows
from ..stringIO.logger.testlogger import *


def jvm_start():
    INFO('[JVM] loading java packages from %s' % CLASSPATH)
    libPath = ''
    try:
        libs = os.listdir(CLASSPATH)
        if len(libs) == 0:
            ERROR('[JVM] no java packages found in %s' % CLASSPATH)
            raise BaseException('no java libs found in %s' % CLASSPATH)
    except:
        INFO('[JVM] no java packages found in %s' % CLASSPATH)
        raise BaseException('[JVM] no java packages found in %s' % CLASSPATH)

    for lib in libs:
        DEBUG('[JVM] %s was found in %s' % (lib, CLASSPATH))
        if isWindows:
            libPath = libPath + os.path.join(CLASSPATH, lib) + ';'
        else:
            libPath = libPath + os.path.join(CLASSPATH, lib) + ':'

    try:
        libs = os.listdir('%s/jars/dependences' % RRSOURCE)
        if len(libs) != 0:
            for lib in libs:
                DEBUG('[JVM] %s was found in %s/jars/dependences' % (lib, RRSOURCE))
                if isWindows:
                    libPath = libPath + os.path.join(os.path.join(RRSOURCE, 'jars', 'dependences'), lib) + ';'
                else:
                    libPath = libPath + os.path.join(os.path.join(RRSOURCE, 'jars', 'dependences'), lib) + ':'
    except:
        WARN('[JVM] no dependency packages in %s/dependences' % RRSOURCE)

    if not jpype.isJVMStarted():
        if isWindows:
            jpype.startJVM(JVMPATH, "-Djava.class.path=%s" % libPath)
        else:
            jpype.startJVM(JVMPATH, "-Djava.class.path=%s" % libPath)

    INFO('[JVM] start jvm result: %s' % bool(jpype.isJVMStarted()))
