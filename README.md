# INFO

This version of the plugin works ONLY with Rhythmbox 2 (last tested: v2.96). You can get the plugin's version for Rhythmbox 3 on [the lotan rhythmbox-ampache repository](https://github.com/lotan/rhythmbox-ampache).
Original source of this plugin : http://code.google.com/p/rhythmbox-ampache/

# Ampache setup

Read Ampache Access Control Lists documentation and create an ACL for RPC (XML API)
	http://ampache.org/wiki/config:acl

# Rhythmbox setup

Create an ampache directory, untar and put files into it then put this directory into 
$HOME/.gnome2/rhythmbox/plugins or /usr/lib/rhythmbox/plugins

Run rhythmbox (with "-D ampache" if you want debug from command line)

Click Edit, select Plugins dialog box, enable "Ampache Library"

Click Configure, enter your informations, for example URL:
	http://test.com/server/xml.server.php

Click on Ampache under Shared, songs should appear in the browser


# COPYRIGHT

Copyright (C) 2008-2010 Rhythmbox Ampache plugin team

Copyright (C) 2008 Seva <seva@sevatech.com>

Portions from Magnatune Rhythmbox plugin
Copyright (C) 2006 Adam Zimmerman <adam_zimmerman@sfu.ca>
Copyright (C) 2006 James Livingston <doclivingston@gmail.com>

Portions from 'git clone http://quickplay.isfound.at'
Copyright (C) 2008 Kevin James Purdy irc://irc.freenode.org/purdyk,isnick


# LICENSE

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2, or (at your option)
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301  USA.
