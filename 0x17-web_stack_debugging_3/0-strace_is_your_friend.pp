# fix the server's bug

exec { 'update settings file':
        command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}

exec { 'restart apache2':
        command  => 'service apache2 restart'
}
