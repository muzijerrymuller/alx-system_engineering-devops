#!/usr/bin/pup
#This Puppet task will guarantee that the Flask package is installed via pip3.
exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
  path    => ['/usr/bin', '/bin'],
}
