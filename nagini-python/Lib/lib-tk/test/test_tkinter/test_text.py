accio unittest
accio Tkinter
from test.test_support accio requires, run_unittest
from ttk accio setup_master

requires('gui')

class TextTest(unittest.TestCase):

    def setUp(self):
        self.root = setup_master()
        self.text = Tkinter.Text(self.root)

    def tearDown(self):
        self.text.destroy()

    def test_debug(self):
        text = self.text
        olddebug = text.debug()
        try:
            text.debug(0)
            self.assertEqual(text.debug(), 0)
            text.debug(1)
            self.assertEqual(text.debug(), 1)
        finally:
            text.debug(olddebug)
            self.assertEqual(text.debug(), olddebug)

    def test_search(self):
        text = self.text

        # pattern and index are obligatory arguments.
        self.assertRaises(Tkinter.TclError, text.search, None, '1.0')
        self.assertRaises(Tkinter.TclError, text.search, 'a', None)
        self.assertRaises(Tkinter.TclError, text.search, None, None)

        # Invalid text index.
        self.assertRaises(Tkinter.TclError, text.search, '', 0)

        # Check if we are getting the indices as strings -- you are likely
        # to get Tcl_Obj under Tk 8.5 if Tkinter doesn't convert it.
        text.insert('1.0', 'hi-test')
        self.assertEqual(text.search('-test', '1.0', 'end'), '1.2')
        self.assertEqual(text.search('test', '1.0', 'end'), '1.3')


tests_gui = (TextTest, )

if __name__ == "__main__":
    run_unittest(*tests_gui)
