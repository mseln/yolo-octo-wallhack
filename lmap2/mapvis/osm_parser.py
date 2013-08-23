#!/usr/bin/python
# 
# osm_parser.py - simple parser to extract nodes and edges from
# osm data.
# 
#----------------------------------------------------------------
# This program is based on Oliver White's program
# pyroute.py 
# Source: http://almien.co.uk/OSM/Routing/
#   python(3) pyroute.py [input OSM file]
#------------------------------------------------------
# Usage: 
#------------------------------------------------------
# Copyright 2007, Oliver White
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#------------------------------------------------------
# Changelog:
#  2007-11-03  OJW  Created
#------------------------------------------------------


import sys
import math 
from xml.sax import make_parser, handler

class GetRoutes(handler.ContentHandler):
  """Parse an OSM file looking for routing information, and do routing with it"""
  def __init__(self):
    """Initialise an OSM-file parser"""
    self.routing = {}
    self.nodes = {}
  def startElement(self, name, attrs):
    """Handle XML elements"""
    if name in('node','way','relation'):
      if name == 'node':
        """Nodes need to be stored"""
        id = int(attrs.get('id'))
        lat = float(attrs.get('lat'))
        lon = float(attrs.get('lon'))
        self.nodes[id] = (lat,lon)
      self.tags = {}
      self.waynodes = []
    elif name == 'nd':
      """Nodes within a way -- add them to a list"""
      self.waynodes.append(int(attrs.get('ref')))
    elif name == 'tag':
      """Tags - store them in a hash"""
      k,v = (attrs.get('k'), attrs.get('v'))
      if not k in ('created_by'):
        self.tags[k] = v
  def endElement(self, name):
    """Handle ways in the OSM data"""
    if name == 'way':
      last = -1
      highway = self.tags.get('highway', '')
      railway = self.tags.get('railway', '')
      oneway = self.tags.get('oneway', '')
      reversible = not oneway in('yes','true','1')

      for i in self.waynodes:
        if last != -1:
          self.addLink(last, i)
          if reversible:
            self.addLink(i, last)
        last = i

  def addLink(self,fr,to):
    """Add a routeable edge to the scenario"""
    # Look for existing
    try:
      if to in self.routing[fr]:
        return
      # Try to add to list. If list doesn't exist, create it
      self.routing[fr].append(to)
    except KeyError:
      self.routing[fr] = [to]

  def get_nodes(self):
    return self.nodes

  def get_edges(self):
    return self.routing