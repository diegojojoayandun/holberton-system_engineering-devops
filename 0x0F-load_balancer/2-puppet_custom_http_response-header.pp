# manifest to automate the task of creating a custom HTTP header response
exec { 'apt-get-update':
  command => '/usr/bin/apt-get -y update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

ufw_rule { 'Allow HTTP':
  action       => 'allow',
  to_ports_app => 80,
  proto        => 'tcp',
}

file_line { 'a':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  require => Package['nginx'],
}

file_line { 'b':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
