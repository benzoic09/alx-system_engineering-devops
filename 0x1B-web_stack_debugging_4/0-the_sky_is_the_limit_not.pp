# Puppet manifest to fix server errors in Nginx server

# Define Nginx configuration file
#file { '/etc/nginx/nginx.conf':
  #ensure  => file,
  #owner   => 'root',
  #group   => 'root',
  #mode    => '0644',
  #content => template('nginx/nginx.conf.erb'),
  #notify  => Service['nginx'],
#}

# Define Exec resource to run the script
exec { 'fix_nginx_errors':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# restart Nginx
-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
