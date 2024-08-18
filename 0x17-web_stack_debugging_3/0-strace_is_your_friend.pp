#Jerry Muller this file fixes a 500 error that comes from apache

exec { 'Resolve Technical Problems Affecting the WordPress Website':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
