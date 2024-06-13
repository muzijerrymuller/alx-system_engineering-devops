#!/usr/bin/pup
#This Puppet task will guarantee that the Flask package is installed via pip3.
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0 Werkzeug==2.1.1',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  path    => ['/usr/bin', '/bin'],
}
