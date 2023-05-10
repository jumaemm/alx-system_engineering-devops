# Replace phpp extensions with php

exec { 'replace_phpp':
  command => 'sed -i s/phpp/php/g var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/bin/'
}

