# init.pp

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
 path    => ['/usr/bin'],
 require => Package['python3-pip'],
}

