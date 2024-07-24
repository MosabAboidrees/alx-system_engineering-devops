# This Puppet manifest configures Nginx to include a custom HTTP header 'X-Served-By'
# with the value being the hostname of the server.

node default {
    # Ensure Nginx is installed
    package { 'nginx':
        ensure => installed,
    }

    # Ensure Nginx service is running and enabled
    service { 'nginx':
        ensure     => running,
        enable     => true,
        require    => Package['nginx'],
        subscribe  => File['/etc/nginx/sites-available/default'],
    }

    # Manage the default site configuration to include the custom header
    file { '/etc/nginx/sites-available/default':
        ensure  => file,
        content => template('nginx/default.erb'),
        notify  => Service['nginx'],
    }

    # Ensure the hostname fact is available
    package { 'facter':
        ensure => installed,
    }
}

# Create a template for the Nginx default site configuration
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/default.erb':
    ensure  => file,
    content => '
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location / {
        add_header X-Served-By <%= @hostname %>;
    }
}
',
}
