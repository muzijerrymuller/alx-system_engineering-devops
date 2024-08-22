# This script ensures that there is no failed requests on the stack
# jerrymuller

exec { 'my first time Altering the limit of files that a stack cann take':
    command  => 'sudo sed -i "s/15/4096/g" /etc/default/nginx; sudo service nginx restart',
    provider => shell,
}
