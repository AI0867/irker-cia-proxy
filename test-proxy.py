#!/usr/bin/env python
import xmlrpclib

message = """
<message>
   <generator>
      <name>Test Generator</name>
      <version>0.01</version>
      <url>http://example.com</url>
   </generator>
   <source>
      <project>testproj</project>
      <branch>testproj:master</branch>
   </source>
   <timestamp>1234567890</timestamp>
   <body>
      <commit>
          <author>test</author>
          <revision>123abcd</revision>
          <files>
              <file>src/abc.sh</file>
              <file>src/def.py</file>
          </files>
          <log>tested some spork actions - http://example.com/</log>
          <url>http://example.com/</url>
      </commit>
   </body>
</message>
"""

svr = xmlrpclib.Server("http://localhost:8000/RPC2")
svr.hub.deliver(message)
