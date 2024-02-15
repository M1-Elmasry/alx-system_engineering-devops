# fix server's bug

exec { 'update settings file':
        provider => 'shell',
        command  => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php && service apache2 restart'
}
