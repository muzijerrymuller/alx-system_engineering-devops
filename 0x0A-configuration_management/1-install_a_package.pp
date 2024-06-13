# #!/usr/bin/env puppet
# This Puppet task will guarantee that the Flask package is installed via pip3.
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}