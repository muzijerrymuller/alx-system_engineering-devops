# This Puppet manifest ensures that Flask version 2.1.0 is installed using pip3.

# Use the python::pip defined type to install Flask.
python::pip { 'flask':
  ensure       => '2.1.0',
  pip_provider => 'pip3',
}
