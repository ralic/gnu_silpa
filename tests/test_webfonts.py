#!/home/smcweb/bin/python
# -*- coding: utf-8 -*-
# Copyright 2009-2010 Santhosh Thottingal <santhosh.thottingal@gmail.com>
# http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import random
import unittest
import sys,os
sys.path.append("../src/")
from silpa.modules import webfonts

class TestDictionary(unittest.TestCase):

    def setUp(self):
		self.webfonts=webfonts.getInstance()

    def testSearch(self):
        self.assertEqual(self.webfonts.get_fonts_list(['Malayalam','English']), "")


if __name__ == '__main__':
    unittest.main()


