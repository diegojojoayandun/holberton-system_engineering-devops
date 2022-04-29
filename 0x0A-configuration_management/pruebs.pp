# kills a process
exec { 'myps':
  command  => '/usr/bin/ps myps',
  provider => 'shell',
  returns  => [0, 1],
}
