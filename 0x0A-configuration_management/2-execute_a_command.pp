#!/usr/bin/pup
#This Puppet script ensures the killmenow process is stopped using pkill within an exec resource.

exec { 'pkill killmenow':
  path     => '/usr/bin',
  command  => 'pkill killmenow',
  provider => shell,
  returns  => [0, 1]
}
