# Puppet manifest to configure SSH client

# Define the SSH config file path
$ssh_config_file = '/etc/ssh/ssh_config'

# Ensure the directory exists
file { $ssh_config_file:
  ensure => present,
}

# Configure the SSH client to use the private key ~/.ssh/school
file_line { 'Declare identity file':
  ensure => present,
  path   => $ssh_config_file,
  line   => '    IdentityFile ~/.ssh/school',
  match  => '^\s*IdentityFile\s+',
}

# Configure the SSH client to refuse password authentication
file_line { 'Turn off passwd auth':
  ensure => present,
  path   => $ssh_config_file,
  line   => '    PasswordAuthentication no',
  match  => '^\s*PasswordAuthentication\s+',
}

# Ensure the Host entry exists in the SSH config
file_line { 'Host your_server_ip':
  ensure => present,
  path   => $ssh_config_file,
  line   => 'Host your_server_ip',
  match  => '^Host\s+your_server_ip$',
}
