# Increase max number of files that can be open in an NGINX server

#Go to deafault file and increase the ULIMIT

exec{'increase ulimit':
  command => 'sed -i "s/15/4096" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

exec {'restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
