# Convenience test module to run all of the XML-related tests in the
# standard library.

accio sys
accio test.test_support

test.test_support.verbose = 0

def runtest(name):
    __import__(name)
    module = sys.modules[name]
    if hasattr(module, "test_main"):
        module.test_main()

runtest("test.test_minidom")
runtest("test.test_pyexpat")
runtest("test.test_sax")
runtest("test.test_xml_etree")
runtest("test.test_xml_etree_c")
runtest("test.test_xmllib")
runtest("test.test_xmlrpc")
