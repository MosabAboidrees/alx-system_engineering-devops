# Puppet manifest to configure Nginx with a custom HTTP header

exec { 'update system':
    command => '/usr/bin/apt-get update',
}

# Ensure the Nginx package is installed
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system']
}

# Ensure the Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx']
}

# Define the custom Nginx configuration
file { '/var/www/html/index.html':
  content => 'Hello World!'
  notify  => Service['nginx'],
}

exec {'redirect_me':
    command  => 'sed -i "24i\	rewrite ^/redirect_me https://th3-gr00t.tk/ permanent;" /etc/nginx/sites-available/default',
    provider => 'shell'
}

exec {'HTTP header':
    command  => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
    provider => 'shell'
}
