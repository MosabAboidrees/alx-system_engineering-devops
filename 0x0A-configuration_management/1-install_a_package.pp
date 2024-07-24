# This Puppet manifest installs Flask version 2.1.0 and Werkzeug version 2.1.1 using pip3.

# Ensure pip3 is installed
package { 'python3-pip':
  ensure  => installed,
}

# Install Flask version 2.1.0
exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['/usr/bin', '/usr/sbin'],
  unless  => '/usr/bin/pip3 show flask | grep Version | grep -q 2.1.0',
  require => Package['python3-pip'],
}

# Install Werkzeug version 2.1.1
exec { 'install_werkzeug':
  command => '/usr/bin/pip3 install werkzeug==2.1.1',
  path    => ['/usr/bin', '/usr/sbin'],
  unless  => '/usr/bin/pip3 show werkzeug | grep Version | grep -q 2.1.1',
  require => Exec['install_flask'],
}
