# Replace lines in a config file
include stdlib

file_line { "Delare private key file":
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '	IdentityFile ~/.ssh/school',
  replace => true,
}

file_line { "disable password auth":
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '	PasswordAuthentication no',
  replace => true,
}
