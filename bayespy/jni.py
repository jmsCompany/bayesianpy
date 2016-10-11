import jpype as jp
import os
import bayespy.utils
import platform

if not jp.isJVMStarted():
    path_to_package = bayespy.utils.get_path_to_parent_dir(__file__)
    separator = ";"
    if platform.system() == "Linux":
        separator = ":"

    classpath = ".{0}{1}{0}{2}".format(separator, os.path.join(path_to_package, 'bin/bayesserver-7.8.jar'),
                                       os.path.join(path_to_package, 'bin/sqlite-jdbc-3.8.11.2.jar'))

    jp.startJVM(jp.getDefaultJVMPath(), "-Djava.class.path={}".format(classpath), "-XX:-UseGCOverheadLimit", "-Xmx6g")

    # so it doesn't crash if called by a Python thread.
    if not jp.isThreadAttachedToJVM():
        jp.attachThreadToJVM()

    bayesServer = jp.JPackage("com.bayesserver")
    sqlLite = jp.JPackage("org.sqlite.JDBC")
    bayesServerInference = jp.JPackage("com.bayesserver.inference")
    bayesServerAnalysis = jp.JPackage("com.bayesserver.analysis")
    bayesServerParams = jp.JPackage("com.bayesserver.learning.parameters")
    bayesServerDiscovery = jp.JPackage("com.bayesserver.data.discovery")
    bayesServerStructure = jp.JPackage("com.bayesserver.learning.structure")